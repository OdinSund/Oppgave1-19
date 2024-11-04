dato1dag = input('Skriv inn en dato, først dagen i måneden: ')
dato1måned = input('Så hvilken måned: ')

dato2dag = input('Skriv inn en til dato, først dagen i måneden: ')
dato2måned = input('Så hvilken måned: ')

if dato1måned<dato2måned:
    print('Riktig rekkefølge!')
elif dato1måned>dato2måned:
    print('Feil rekkefølge!')
elif dato1måned == dato2måned:
    if dato1dag<dato2dag:
        print('Riktig rekkefølge!')
    elif dato1dag>dato2dag:
        print('Feil rekkefølge!')
    else:
        print('Samme Dato!')
