


def printNtimes(n: int):
    if n > 0:
        print("Coding Ninjas ")
        printNtimes(n - 1)
    else:
        pass

sum1 = 0
def sumFirstN(n: int) -> int:
    global sum1
    sum1 = sum1 + n
    if n > 0:
        print("sum1 ::", sum1, " ", n)
        return sumFirstN(n - 1)
        print("ans ::", ans)
    else:
        print("sum2 ::", sum1)
        return sum1

def sumFirstN1(n: int) -> int:
    print("n ::", n)
    if n > 0:
        ans = sumFirstN1(n - 1)
        print("sum2 ::", ans)
        return (n + ans)
    else:
        return n

def factorials(n):
    ans = 1
    # for i in range(1, n+1):
    #     print("i ::", i)
    #     ans = ans * i
    print("n ::", n)
    if n > 0:
        return (n * factorials(n-1))
    else:
        return 1



# ans = printNtimes(5)
# sumation = sumFirstN(3)
print(sumFirstN1(3))
#print(factorials(5))

