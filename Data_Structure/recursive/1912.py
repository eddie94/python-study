def fact(num):

    if num > 1:
        num *= fact(num-1)

    return num

print(fact(5))