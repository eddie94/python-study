from functools import reduce

def collapse(data):
    return reduce(lambda x,y: x+y, data)

def slice(string, n):
    '''

    :param string: 자르고자 하는 문자열
    :param n: 문자열을 자르는 최소 단위
    :return: 자르고 난 뒤의 문자열을 리스트에 담고 반환
    '''
    temp = []
    i=n

    #문자열의 인덱스를 n만큼 쪼개서 temp에 저장
    #인덱스가 문자열의 길이를 초과했을 경우 다음으로 넘어감
    while i<= len(string):
        temp.append(string[(i-n):i])
        i += n

    #자르고 난 뒤 남은 문자가 있으면 temp의 마지막 요소로 남은 문자들을 넣어줌
    try:
        if string[(i-n)] != '':
            temp.append(string[(i-n):])
    except IndexError:
        pass

    return temp