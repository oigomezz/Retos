T = int(input().strip())
str_input = input().strip()
v = list(range(1, T + 1))
songindex = 0
pindex = 0

while True:
    if pindex == len(v):
        pindex = 0
    if songindex == len(str_input):
        songindex = 0
    if len(v) == 1:
        print(v[0])
        break
    if str_input[songindex] == 'a':
        pindex += 1
    else:
        v.pop(pindex)
    songindex += 1
