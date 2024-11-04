datotall1 = input('Skriv inn en dato på denne måten: 05/03/07\n').split("/")
datotall2 = input('Skriv inn en til dato på denne måten: 05/03/07\n').split("/")

if datotall1[2] < datotall2[2]:
     print('Riktig rekkefølge!')
elif datotall1[2] > datotall2[2]:
     print('Feil rekkefølge!')
elif datotall1[2] == datotall2[2]:
    if datotall1[1] < datotall2[1]:
         print('Riktig rekkefølge!')
    elif datotall1[1] > datotall2[1]:
         print('Feil rekkefølge!')
    elif datotall1[1] == datotall2[1]:
        if datotall1[0] < datotall2[0]:
             print('Riktig rekkefølge!')
        elif datotall1[0] > datotall2[0]:
             print('Feil rekkefølge!')
        elif datotall1[0] == datotall2[0]:
             print('Samme dag!')


