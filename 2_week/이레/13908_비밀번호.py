result = 0
start = 10
n, m = map(int, input().split())
k = list(map(int, input().split()))


def fact(a):
    temp = 1
    for i in range(a):
        temp *= i + 1
    return temp


for i in range(m + 1):
    result += (int)(fact(m) / (fact(m - i) * fact(i))) * pow(start, n) * ((-1) ** i)
    start -= 1
print(result)
