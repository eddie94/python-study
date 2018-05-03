def life_or_death(board):

    board = board.split()
    board_list = [board[i:i+10] for i in range(0,len(board),10)]

    x_axis = 0
    y_axis = len(board_list)-2

    LOD=[]
    line = []
    cnt = 0

    for i in range(len(board_list[0])):  #x축 이동
        for j in range(1,len(board_list)): #y축 이동

            if int(board_list[-1][i]) == 1 and int(board_list[y_axis][x_axis]) > 0:

                line.append('crash')
                LOD.append(x_axis+1)
                break

            elif int(board_list[-1][i]) == 1 and int(board_list[y_axis][x_axis]) < 0:

                line.append('fall')
                LOD.append(x_axis+1)
                break

            elif int(board_list[-1][i]) == 1 and int(board_list[y_axis][x_axis]) == 0:

                cnt += 1

            y_axis -= 1

        if cnt == len(board_list)-1:

            line.append('safe')
            LOD.append(x_axis+1)

        cnt = 0
        x_axis += 1
        y_axis = len(board_list)-2

    return line, LOD

a = '''0 0 0 0 0 0 0 0 0 0 
0 2 0 0 0 0 0 0 0 0 
0 0 -1 0 0 0 0 0 2 0 
0 0 0 0 0 0 0 6 0 0 
0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 -4 2 0 0 0 
0 0 2 0 0 0 0 0 0 0 
0 0 0 0 3 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 
1 1 0 0 1 1 0 1 0 1 
'''

line, LOD = life_or_death(a)

for unit,life in zip(LOD, line):
    print(unit,life)