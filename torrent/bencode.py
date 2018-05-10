import types
from util import *

def stringlength(string, index = 0):

    try:
        colon = string.find(':',index)
    except ValueError:
        raise BencodeError('Decode','Malformed expression',data)

    num = [a for a in string[index:colon] if a.isdigit()]
    n = int(collapse(num))

    return len(num) + 1 + n

def walk(exp, index=1):

    if exp[index] == 'i':
        endchar = exp.find('e',index)
        return walk(exp,endchar+1)
    elif exp[index].isdigit():
        strlength = stringlength(exp,index)
        return walk(exp,index+strlength)
    elif exp[index] == 'l' or exp[index] == 'd':
        endsub = walk(exp[index:],1)
        return walk(exp,index+endsub)
    elif exp[index]=='e':
        index+=1
        return index

def inflate(exp):

    if exp == '':
        return []

    if ben_type(exp) == int:
        end = exp.find('e')
        x = exp[:end+1]
        xs = inflate(exp[end+1:])
    elif ben_type(exp) == str:
        strlength = stringlength(exp)
        x = exp[:strlength]
        xs = inflate(exp[strlength:])
    elif ben_type(exp) == list or ben_type(exp) == dict:
        end = walk(exp)
        x = exp[:end]
        xs = inflate(exp[end:])

    return [x] + xs

def ben_type(exp):

    if exp[0] == 'i':
        return int
    elif exp[0].isdigit():
        return str
    elif exp[0] == 'l':
        return list
    elif exp[0] == 'd':
        return dict

def check_type(exp, datatype):

    try:
        assert type(exp) == datatype
    except AssertionError:
        raise BencodeError('Encode','Malformed expression',exp)

def check_ben_type(exp, datatype):

    try:
        assert ben_type(exp) == datatype
    except AssertionError:
        return BencodeError('Decode','Malformed expression',exp)

class BencodeError(Exception):
    def __init__(self,mode, value, data):

        assert mode in ["Encode",'Decode']

        self.mode = mode
        self.value = value
        self.data = data

    def __str__(self):

        return repr(self.mode+': '+self.value+' : '+str(self.data))

def encode_int(data):
    check_type(data, int)

    return 'i'+str(data)+'e'

def decode_int(data):
    check_ben_type(data, int)

    try:
        end = data.index('e')
    except ValueError:
        raise BencodeError('Decode', 'Cannot Find end of Integer expression', data)

    t = data[1:end]

    if len(t) > 1 and t[0] == '0':
        raise BencodeError('Decode', 'Malformed expression', data)

    return int(t)

def encode_str(data):
    check_type(data, str)

    return str(len(data))+':'+data

def decode_str(data):

    try:
        colon = data.find(':')
    except ValueError:
        raise BencodeError('Decode','Badly formed expression',data)

    strlength = stringlength(data)

    return data[colon + 1 : strlength]

def encode_list(data):
    check_type(data,list)

    if data == []:
        return 'le'

    temp = [encode(item) for item in data]
    return 'l' + collapse(temp) + 'e'

def decode_list(data):

    if data == 'le':
        return []

    result = []

    temp = inflate(data[1:-1])
    for i in range(len(temp)):
        print(temp[i])
        print(decode(temp[i]))
        result.append(decode(temp[i]))

    return result


def encode_dict(data):
    check_type(data,dict)

    if data == {}:
        return 'de'

    temp = [encode_str(key) + encode_str(data[key]) for key in sorted(data.keys())]
    return 'd'+collapse(temp)+'e'

def decode_dict(data):

    if data == 'de':
        return {}

    data = data[1:-1]

    temp = {}
    terms = inflate(data)
    print(terms)

    cnt = 0
    while cnt != len(terms):
        temp[decode_str(terms[cnt])] = decode(terms[cnt+1])
        cnt+=2

    return temp

encode_functions = {int : encode_int,
                    str : encode_str,
                    list : encode_list,
                    dict : encode_dict}

decode_functions = {int : decode_int,
                    str : decode_str,
                    list : decode_list,
                    dict : decode_dict}

#아래 두 함수는 들어오는 데이터 타입에 따라 함수를 호출
#함수명은 *_functions안에 들어가 있다
def encode(data):

    try:
        return encode_functions[type(data)](data)
    except KeyError:
        raise BencodeError('Encode','Unknown data type',data)

def decode(data):

    try:
        return decode_functions[ben_type(data)](data)
    except KeyError:
        raise BencodeError('Decode','Unknown data type',data)

