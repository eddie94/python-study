class stack_pointer_exception(Exception):

    def __init__(self,msg):
        self.msg = msg

    def __str__(self):
        return self.msg

class stack():

    def __init__(self):
        self.data = []
        self.size = 0
        self.index = 0
        self.stack_pointer = 0

    def __iter__(self):

        return self

    def __next__(self):

        if self.index >= self.size:
            raise StopIteration

        n = self.data[self.index]
        self.index += 1
        return n

    def __len__(self):
        return self.size

    def __repr__(self):

        return str(self.data)

    def Push(self,value):
        self.data.append(value)
        self.stack_pointer += 1
        self.size += 1

    def Pop(self):

        if self.stack_pointer == 0:
            raise stack_pointer_exception('NO ELEMENT IN STACK. UNABLE TO POP')

        data = self.data.pop()
        self.stack_pointer -= 1
        self.size -= 1

        return data

def classify_integers(n, num):

    classified_number = stack()

    # for i in range(1,n+1):
    #     if classified_number.stack_pointer != 0 and classified_number.stack_pointer % 3 == 0:
    #         classified_number.Push(',')
    #     else:
    #         classified_number.Push(num % (pow(10,i)))
    #         num -= num % (pow(10,i))

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