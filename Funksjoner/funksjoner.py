def Adder(tall1, tall2):
    result = tall1 + tall2
    return result

a = 3
b = 4

print("Summen av " + str(a) + " og " + str(b) + " er " + str(Adder(a, b)))

a = 12
b = 20

print("Summen av " + str(a) + " og " + str(b) + " er " + str(Adder(a, b)))

def tellForekomst(minTekst, minBokstav):
    svar = minTekst.count(minBokstav)
    return svar

minTekst = input("Skriv inn en setning her: ")
minBokstav = input("Skriv en bokstav her: ")
print(tellForekomst(minTekst, minBokstav))
