class allocation_error(Exception):
    pass

class underflow(Exception):
    pass

class overflow(Exception):
    pass

class queue():

    def __init__(self,size,alloc='ring'):

        self.front = 0
        self.rear = 0
        self.data = [None for i in range(size)]
        self.index = 0
        self.size = size
        self.data_size = 0
        self.alloc = alloc

    def __iter__(self):

        return self

    def __next__(self):

        if self.index >= self.data_size:
            raise StopIteration

        n = self.data[self.index]
        self.index += 1
        return n

    def __repr__(self):

        return str(self.data)

    def __len__(self):

        return self.data_size

    def Push(self,value):

        if self.alloc == 'dynamic':

            if self.is_full():
                data = [None for i in range(self.size*2)]
                data[:self.size] = self.data
                self.data = data
                self.data[self.front] = value
                self.size *= 2
                self.front += 1
                self.data_size += 1
            else:
                self.data[self.front] = value
                self.front += 1
                self.data_size += 1

        elif self.alloc == 'ring':

            if self.is_full():
                raise overflow
            else:
                if self.front == self.size-1:
                    self.front = (self.front + 1) % self.size
                else:
                    self.front += 1
                self.data[self.front] = value
                self.data_size += 1

        else:
            raise allocation_error

    def Pop(self):

        if self.alloc == 'dynamic':

            if self.is_empty():

                raise underflow

            else:
                data = self.data[self.rear]
                self.data[self.rear] = None
                self.rear += 1
                self.data_size -= 1
                return data

        elif self.alloc == 'ring':

            if self.is_empty():
                raise underflow
            else:
                if self.rear == self.size-1:
                    self.rear = (self.rear + 1) % self.size
                else:
                    self.rear += 1
                data = self.data[self.rear]
                self.data[self.rear] = None
                self.data_size -= 1
                return data

        else:
            raise allocation_error

    def is_full(self):

        if self.alloc == 'dynamic':

            if self.front == self.size:
                return True
            else:
                return False

        elif self.alloc == 'ring':

            if (self.front+1) % self.size == self.rear:
                return True
            else:
                return False
        else:
            raise allocation_error

    def is_empty(self):

        if self.alloc == 'dynamic':

            if self.front == self.rear:
                self.front = 0
                self.rear = 0
                return True
            else:
                return False

        elif self.alloc == 'ring':

            if self.front == self.rear:
                self.front = 0
                self.rear = 0
                return True
            else:
                return False

        else:
            raise allocation_error
