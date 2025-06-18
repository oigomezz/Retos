import math

def check(a, b):
    if a > b:
        a, b = b, a
    a *= a
    a *= 2
    temp = math.sqrt(a)
    return temp > b


if __name__ == "__main__":
    n = int(input())
    first = []
    second = []
    for i in range(1, n + 1):
        a, b = map(int, input().split())
        if a == 1:
            first.append(b)
        else:
            second.append(b)
    
    first.sort()
    second.sort()
    
    left = 0
    right = 0
    result = 0
    
    while left < len(first) and right < len(second):
        if check(first[left], second[right]):
            result += 1
            left += 1
            right += 1
        elif first[left] < second[right]:
            left += 1
        else:
            right += 1
    
    print(result)
