first_row = input()
second_row = input()
thrid_row = input()

c = flag = 0
m = '0'

O = first_row.count('O') + second_row.count('O') + thrid_row.count('O')
ex = first_row.count('X') + second_row.count('X') + thrid_row.count('X')

if O > ex or O+1 < ex:
    print('Wait, what?')
else:
    if (first_row[0] == second_row[0] == thrid_row[0] or first_row[0] == first_row[1] == first_row[2]) and (first_row[0] == 'X' or first_row[0] == 'O'):
        m = first_row[0]
        c += 1

    if (first_row[0] == second_row[1] == thrid_row[2] or first_row[2] == second_row[1] == thrid_row[0] or first_row[1] == second_row[1] == thrid_row[1] or second_row[0] == second_row[1] == second_row[2]) and (second_row[1] == 'X' or second_row[1] == 'O'):
        if (m == '0') or (m == second_row[1] == 'X'):
            m = second_row[1]
        elif (m != second_row[1]) and (m != '0'):
            flag = 1
        c += 1

    if (first_row[2] == second_row[2] == thrid_row[2] or thrid_row[0] == thrid_row[1] == thrid_row[2]) and (thrid_row[2] == 'X' or thrid_row[2] == 'O'):
        if (c == 2) or (m != thrid_row[2]) and (m != '0'):
            flag = 1
        elif (m == thrid_row[2] == 'X') and (c == 1) or (c == 0):
            m = thrid_row[2]
        c += 1

    if (((c == 3) or (flag == 1)) or ((O == ex) and (m == 'X')) or ((ex > O) and (m == 'O'))):
        print('Wait, what?')
    elif (m == '0'):
        if (O+ex < 9):
            print("X's turn.") if (O == ex) else print("O's turn.")
        else:
            print("It's a draw.")
    else:
        print(m, 'won.')
