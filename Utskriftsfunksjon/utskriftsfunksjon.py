

def utskrift():
    navn = input('Skriv inn ditt navn: ')
    bosted = input('Hvor kommer du fra? ')

    print('Hei ' + navn + '. Du er fra ' + bosted)

for i in range(3):
    utskrift()