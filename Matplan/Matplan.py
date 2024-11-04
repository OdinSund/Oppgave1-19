Dict = {"Sjaman Durek": ["Brødskiver", "Yoghurt", "Kylling og ris"], "Magne Kobbevik": ["Vaniljesaus", "Brødskive", "Taco"], "Kurt Kåre Johnny": ["Wienerpølse", "Banan", "Biff"] }

def BeboerInfo():
    print(Dict.keys())
    navn = input("Skriv navnet til en beboer: ")
    
    try:
        x = Dict[navn]
        print(x)
    except:
        print("Den personen er ikke her")
    

BeboerInfo()