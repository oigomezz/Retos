t = int(input())
st = "abcdefghijklmnopqrstuvwxyz"
for i in range(t):
    res = input()
    nm = res[::-1]
    if (res == nm):
        print("Palindrome")
    else:
        s = 1
        for i in res:
            au = st.find(i)
            # print(au)
            s = s * (au+1)
        print(s)
