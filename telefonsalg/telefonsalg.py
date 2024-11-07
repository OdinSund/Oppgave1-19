def innlesing(filnavn):
    salgsdata = {}
    with open(filnavn, 'r') as fil:
        for linje in fil:
            navn, salg = linje.strip().split(" ")
            salgsdata[navn] = int(salg)
    return salgsdata

def maanedensSalgsperson(ordbok):
    bestansatt = max(ordbok, key=ordbok.get)
    bestantall = ordbok[bestansatt]
    print(f"Maanedens ansatt er {bestansatt}, som solgte {bestantall} telefoner!")

def totaltAntallSalg(ordbok):
    return sum(ordbok.values())

def gjennomsnittSalg(ordbok):
    totalsalg = totaltAntallSalg(ordbok)
    selgere = len(ordbok)
    gjennomsnitt = totalsalg / selgere
    return (selgere, gjennomsnitt)

def hovedprogram():
    filnavn = innlesing('salgstall.txt')
    antallselgere = gjennomsnittSalg(innlesing('salgstall.txt'))[0]
    gjennomsnitt = int(gjennomsnittSalg(innlesing('salgstall.txt'))[1])
    maanedensSalgsperson(filnavn)
    totalsalg = totaltAntallSalg(filnavn)
    print(f'Denne maaneden har {antallselgere} selgere solgt gjennomsnittlig {gjennomsnitt} telefoner og totalt {totalsalg}')

hovedprogram()


