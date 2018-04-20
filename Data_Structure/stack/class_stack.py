class stack_pointer_exception(Exception):

    def __init__(self,msg):
        self.msg = msg

    def __str__(self):
        return self.msg

class alloc_error(Exception):

    def __init__(self,msg):
        self.msg = msg

    def __str__(self):
        return self.msg

class size_error(Exception):

    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

class stack():

    def __init__(self,N=0,alloc='dynamic'):
        self.data = []
        self.current_size = 0
        self.alloc = alloc
        self.size = self.dynamic_allocate(N, alloc)
        self.index = 0
        self.stack_pointer = 0

    def __iter__(self):

        return self

    def __next__(self):

        if self.index >= self.current_size:
            raise StopIteration

        n = self.data[self.index]
        self.index += 1
        return n

    def __len__(self):
        return self.current_size

    def __repr__(self):

        return str(self.data)

    def dynamic_allocate(self, N, alloc):

        if self.alloc == 'dynamic':
            return self.current_size
        elif self.alloc == 'fixed':
            return N
        else:
            raise alloc_error('KEY ERROR : INSERT dynamic, fixed, OR LEAVE IT BLANK')

    def is_full(self):
        if self.stack_pointer == self.size:
            return True
        else:
            return False

    def is_empty(self):

        if self.stack_pointer == 0:
            return True
        else:
            return False

    def Push(self,value):

        if self.alloc == 'dynamic':
            self.data.append(value)
            self.stack_pointer += 1
            self.current_size += 1
        elif not self.is_full() and self.alloc == 'fixed':
            self.data.append(value)
            self.stack_pointer += 1
            self.current_size += 1
        else:
            raise stack_pointer_exception('STACK IS FULL')

    def Pop(self):

        if self.stack_pointer == 0:
            raise stack_pointer_exception('NO ELEMENT IN STACK. UNABLE TO POP')

        data = self.data.pop()
        self.stack_pointer -= 1
        self.current_size -= 1

        return data

    def peek(self):

        return self.data[-1]
