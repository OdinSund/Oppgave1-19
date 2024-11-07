class Motorsykkel:
    def __init__(self, merke, regnr, kmstand):
        self.merke = merke
        self.regnr = regnr
        self.kmstand = kmstand

    def kjor(self, km):
        self.kmstand += km

    def hentKilometerstand(self):
        return self.kmstand

    def skrivUt(self):
        print(f'Merke: {self.merke}')
        print(f'Registreringsnummer: {self.regnr}')
        print(f'Kilometerstand {self.kmstand}\n')

motorsykkel4 = Motorsykkel('KTM', 'GH1234', 10972)