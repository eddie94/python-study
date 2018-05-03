from random import randint

def get_submitted_tower(N):
    '''

    :param N: 타워의 개수
    :param h:  타워의 높이
    '''
    submit = []     #수신한 타워의 위치를 기록하는 리스트
    towers = []     #랜덤한 높이의 타워를 기록하는 리스트

    #랜덤한 높이를 받아서 리스트에 추가
    for i in range(N):
        h = randint(1,100)
        towers.append(h)

    towers.reverse()    #계산의 편의상 타워를 한번 뒤집어줌

    #타워의 첫부분부터 값을 비교해 다음값이 현재의 값보다 크면
    #submit에 위치를 저장
    for i in range(len(towers)):
        if i == len(towers)-1:
            submit.append(0)
        else:
            for j in range(1,len(towers)-i):
                if towers[i] <= towers[i+j]:
                    submit.append(len(towers)-i-j)
                    break
            else:
                submit.append(0)

    submit.reverse()        #뒤집어진 위치를 다시 뒤집음

    for i in submit:
        print(i,end='')

tower = get_submitted_tower(5)