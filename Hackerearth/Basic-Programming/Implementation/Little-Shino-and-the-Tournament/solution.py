n, q = map(int, input().split())
strength = list(map(int, input().split()))

fighters = []
for i in range(n):
    fighters.append({'strength': strength[i], 'fights': 0})

fighters_left = 1
while fighters_left > 0:
    fighters_left = fighter_id = -1

    for i in range(n):
        if fighters[i]['strength'] > 0:
            fighters_left += 1

            if fighter_id == -1:
                fighter_id = i
            else:
                if fighters[fighter_id]['strength'] < fighters[i]['strength']:
                    fighters[fighter_id]['strength'] = -1
                else:
                    fighters[i]['strength'] = -1

                fighters[fighter_id]['fights'] += 1
                fighters[i]['fights'] += 1
                fighter_id = -1

for _ in range(q):
    i = int(input().strip())
    print(fighters[i - 1]['fights'])
