t = int(input())
results = []
for _ in range(t):
    ammo, obs = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(obs):
        if A[i] == 0:
            ammo -= 1
        if A[i] == 1:
            ammo += 2
        if ammo != 0 and i == obs - 1:
            results.append(f"Yes {ammo}")
            break
        if ammo == 0 and i != obs - 1:
            results.append(f"No {i + 1}")
            break
        if ammo == 0 and i == obs - 1:
            results.append(f"Yes {ammo}")
            break

for result in results:
    print(result)
