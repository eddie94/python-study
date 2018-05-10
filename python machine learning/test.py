def check_if_list(a):

    for x in a:
        if type(x) == list:
            return True
    else:
        return False

def rev(a):

    if type(a) == list and check_if_list(a):

        for x,i in zip(a,range(len(a))):
            if type(x) == list:
                a[i] = rev(a[i])

    elif type(a) == list and not check_if_list(a):
        a.reverse()
        return a
    else:
        pass

    a.reverse()
    return a

print(rev([[1,[1,2],[1,2,3,4,5],5,[3,4],[5,6]]]))