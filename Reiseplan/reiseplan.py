steder = []
klesplagg = []
avreisedatoer = []
reiseplan = [steder, klesplagg, avreisedatoer]

for i in range(5):
    sted = input("Skriv et sted du vil reise til: ")
    steder.append(sted)

for i in range(5):
    klaer = input("Skriv hva du vil ha på deg: ")
    klesplagg.append(klaer)

for i in range(5):
    dato = input("Skriv når du vil: ")
    avreisedatoer.append(dato)

for i in range(len(reiseplan)):
    print(reiseplan[i])
    

uinput = int(input("Hvilken liste vil du hente info fra (1-3): ")) - 1

if uinput < 2 and uinput >= 0:

    i1 = reiseplan[uinput]
    uinput = int(input("Hvilken indeks vil du ha? (1-5): ")) - 1

    if uinput < 4 and uinput >= 0:
        i2 = i1[uinput]
        print(i1,i2)

    else:
        print("Ugyldig Input!")
else:
    print("Ugyldig Input!")