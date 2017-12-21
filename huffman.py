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

def insert_list(list, index, value):
    
    '''
    리스트의 원하는 위치에 원하는 값을 삽입하는 함수
    '''

    new_list = []
    if index is not 0:

        for i in range(index):
            new_list.append(list[i])
            
        new_list.append(value)

        for i in range(len(new_list)-1,len(list)):
            new_list.append(list[i])

    elif index == 0:
        new_list.append(value)
        for i in range(len(list)):
            new_list.append(list[i])
    else:
        pass

    return new_list

def huffman(prob_list):

    new_list = prob_list
    end = False
    length = len(prob_list)-1
    
    while not end:
        
        add_prob = new_list[-1] + new_list[-2]

        new_list = []
        
        for i in range(length):
            
            if prob_list[i] <= add_prob:
                new_list = insert_list(new_list, i, add_prob)
            elif prob_list[i] > add_prob:
                new_list.append(prob_list[i])
            else:
                pass
                
        if len(new_list) == 2:
            end = True
        else:
            print(new_list)
            length -= 1
        
    return new_list
                
    

prob_list = sort(a,b,c,d,e)

huff = huffman(prob_list)
print(huff)


