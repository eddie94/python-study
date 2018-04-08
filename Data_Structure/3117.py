from Data_Structure.class_stack import *

def delete_zero():

    k = int(input('input number'))

    myList = stack()

    for i in range(k):

        num = int(input('number?'))

        if num == 0:
            myList.Pop()
        else:
            myList.Push(num)

    sum = 0

    for num in myList:
        sum += num

    return sum

print(delete_zero())