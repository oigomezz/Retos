t = int(input())
for i in range(t):
    PDF_in_Pendrive = 1
    PDF_in_Computer = 1
    count = 1
    Computer, Pendrive = (int(x) for x in input().split())
    while PDF_in_Computer < Computer:
        if PDF_in_Computer == PDF_in_Pendrive:
            PDF_in_Computer *= 2
        else:
            PDF_in_Computer += PDF_in_Pendrive
            if PDF_in_Pendrive < Pendrive:
                PDF_in_Pendrive += PDF_in_Pendrive
            if PDF_in_Pendrive > Pendrive:
                PDF_in_Pendrive = Pendrive
            count += 1
    if Computer == 1:
        count = 0
    print(count)
