a = 0.2
b = 0.1
c = 0.2
d = 0.4
e = 0.1

def sort(*args):

    prob_list = []
    
    for prob in args:
        prob_list.append(prob)

    prob_list.sort()
    prob_list.reverse()

    return prob_list

def insert_list(my_list, index, value):
    
    '''
    리스트의 원하는 위치에 원하는 값을 삽입하는 함수
    '''

    new_list = []
    if index is not 0:

        for i in range(index):
            new_list.append(my_list[i])
            
        new_list.append(value)

        for i in range(len(new_list)-1,len(my_list)):
            new_list.append(my_list[i])

    elif index == 0:
        new_list.append(value)
        for i in range(len(my_list)):
            new_list.append(my_list[i])
    else:
        pass

    return new_list

def huffman_code(prob_list, bit):

    new_list = prob_list
    end = False
    length = len(prob_list)-1
    code_list = []
    track = bit
    
    while not end:
        
        add_prob = new_list[-1] + new_list[-2]
        print(new_list)
        if track > len(new_list)-1:
            pass
        elif track == len(new_list) -1:
            code_list.append(0)
        elif track == len(new_list):
            code_list.append(1)
        else:
            pass
        
        new_list = []
        index = []
        index_num = 0
        
        for i in range(length-1):
            
            if prob_list[i] <= add_prob:
                index.append(i)
            else:
                pass
            new_list.append(prob_list[i])
            
        index_num = index[0]
        new_list = insert_list(new_list, index_num, add_prob)

        
        if len(new_list) == 2:
            end = True
        else:
            length -= 1
        
    return new_list

prob_list = sort(a,b,c,d,e)

huff = huffman_code(prob_list, 0)
print(huff)
