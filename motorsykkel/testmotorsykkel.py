from main import Motorsykkel

def hovedprogram():
    motorsykkel1 = Motorsykkel('Ducati', 'BL8529', 734)
    motorsykkel2 = Motorsykkel('Kawasaki', 'GF0937', 6401)
    motorsykkel3 = Motorsykkel('Harley Davidson', 'DF0379', 80429)

    motorsykkel1.skrivUt()
    motorsykkel2.skrivUt()
    motorsykkel3.skrivUt()

    motorsykkel3.kjor(10)
    print(motorsykkel3.hentKilometerstand())


hovedprogram()