houses = int(input())
village = input().strip()
if 'HH' in village:
    print('NO')
else:
    print('YES')
    print(village.replace('.', 'B'))
