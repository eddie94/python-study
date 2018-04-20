from Data_Structure.class_stack import *

def classify_integers(n, num):

    classified_number = stack()

    i=1

    while i <= n:

        if classified_number.stack_pointer != 0 and classified_number.stack_pointer % 4 == 3:
            classified_number.Push(',')
        else:
            classified_number.Push(int((num%(pow(10,i)))/pow(10,i-1)))
            num -= num%(pow(10,i))
            i += 1

    string = ''

    for i in range(len(classified_number)):
        data = classified_number.Pop()
        string+=str(data)

    return string

a = classify_integers(8,12345678)
print(a)