def ratio(string):
    k = len(string)
    string = string[:-4]
    jhool = [i for i in string if (i not in "AEIOUaeiou")]
    return str(len(jhool))+"/"+str(k)


t = int(input())
for i in range(t):
    value = input().strip()
    print(ratio(value))
