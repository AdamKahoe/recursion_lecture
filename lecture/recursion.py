# def recursion(num):
#     recursion(num)

def countdown(num):
    for i in range(num, -1, -1):
        print(i)

# countdown(10)

def recCountdown(num):
    if num == 0:
        return num
    print(num)
    return recCountdown(num - 1)

print(recCountdown(10))

# write function that given a number that adds all the numbers to that number

def sumofNum(num):
    sum = 0
    for i in range(num + 1):
        sum += i
    return sum

print(sumofNum(4))

def recSumofNum(num):
    if num == 0:
        return num
    return num + recSumofNum(num - 1)

print(recSumofNum(4))

# 4 + recSumofNum(num -1)
# 4 + 3 + recSumofNum(3-1)
# 4 + 3 + 2 + recSumofNum(2-1)
# 4 + 3 + 2 + 1 + recSumofNum(1-1)
# 4 + 3 + 2 + 1 + 0


def rfib(num):
    if num == 1 or num == 2:
        return 1
    # num -= 1
    return rfib(num-1) + rfib(num-2)

print(rfib(8))

# rfib(8-1) + rfib(8-2)
# refib(7-1) + rfib(7-2)

# rfib(6-1) + rfib(6-2)
# rfib(5-1) + rfib(5-2) + rfib(4-1) + rfib (4-2)
# rfib(4-1) + rfib(4-2)

# fib = (number before it) + (number 2 times before it)