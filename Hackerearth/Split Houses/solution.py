houses = int(input())
village = input()

if 'HH' in village:
    print('NO')
else:
    print('YES')
    print(village.replace('.', 'B'))
