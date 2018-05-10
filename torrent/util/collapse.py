from functools import reduce

def collapse(data):
    return reduce(lambda x,y: x+y, data)