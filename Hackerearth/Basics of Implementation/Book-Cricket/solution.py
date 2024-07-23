# To rotate the plater's turn
def rotate(curr_pyr):
    temp = curr_pyr[0]
    curr_pyr[0] = curr_pyr[1]
    curr_pyr[1] = temp


# To switch the current striker to next player waiting
def switch(curr_pyr):
    curr_pyr[0] = max(curr_pyr)+1


for t in range(1, int(input())+1):
    n, p = map(int, input().split())
    arr = input()
    ctr = 0

    # Creating player scoreboard
    dict = {}
    for i in range(p):
        dict[f'Player {i+1}'] = 0

    # Keeping track of latest current player
    curr_pyr = [1, 2]

    # Logic of game as requirement
    for i in range(len(arr)):
        ctr += 1
        if arr[i] == '0':
            pass
        elif arr[i] == '1':
            dict[f'Player {curr_pyr[0]}'] += 1
            rotate(curr_pyr)
        elif arr[i] == '2':
            dict[f'Player {curr_pyr[0]}'] += 2
        elif arr[i] == '4':
            dict[f'Player {curr_pyr[0]}'] += 4
        elif arr[i] == '6':
            dict[f'Player {curr_pyr[0]}'] += 6
        elif arr[i] == 'W':
            # Negative the OUTED players so it'll be easy to identify who to not append "*"
            dict[f'Player {curr_pyr[0]}'] = dict[f'Player {curr_pyr[0]}']*-1
            switch(curr_pyr)
        if ctr == 6:
            rotate(curr_pyr)
            ctr = 0

    print("Case "+str(t)+":")
    # If only two players, chances of second player never get to play while still not OUTED is high so need to isolate this case
    if max(curr_pyr) == 2:
        for i in range(1, max(curr_pyr)+1):
            print("Player "+str(i)+": "+str(dict[f'Player {i}'])+"*")
    # Based on player's scoreboard, OUTED will have negative score, hence no need to append "*", rest will have "*" meaning not OUTED yet
    else:
        for i in range(1, max(curr_pyr)+1):
            if dict[f'Player {i}'] <= 0:
                print("Player "+str(i)+": "+str((dict[f'Player {i}'])*-1))
            else:
                print("Player "+str(i)+": "+str(dict[f'Player {i}'])+"*")
    # As for those who did not even enter the field, they will just be "DNB"
    for i in range(max(curr_pyr)+1, len(dict)+1):
        print(f"Player {i}: DNB")
