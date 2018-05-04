def fivonacci(num):

    if num == 1 or num == 0:
        return num
    else:
        return fivonacci(num-1) + fivonacci(num-2)

print(fivonacci(5))