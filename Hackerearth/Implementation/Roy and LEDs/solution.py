T, R, G, B = [int(s) for s in input().split(" ")]
colors = []
flag_R, flag_G, flag_B = 0, 0, 0
for t in range(T):
    if t % R == 0 and t >= R:
        flag_R = abs(flag_R-1)

    if t % G == 0 and t >= G:
        flag_G = abs(flag_G-1)

    if t % B == 0 and t >= B:
        flag_B = abs(flag_B-1)

    colors.append([flag_R, flag_G, flag_B])

print(str(colors.count([1, 0, 0]))+" "+str(colors.count([0, 1, 0]))+" "+str(colors.count([0, 0, 1]))+" "+str(colors.count([1, 1, 0])) +
      " "+str(colors.count([0, 1, 1]))+" "+str(colors.count([1, 0, 1]))+" "+str(colors.count([1, 1, 1]))+" "+str(colors.count([0, 0, 0])))
