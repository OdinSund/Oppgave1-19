def RegnUtPris():
    navn = input("Hva er navnet ditt?")
    alder = int(input("Hvor gammel er du?"))
    billettpris = 0
    if alder <= 17:
        billettpris = 30
    elif alder > 17 and alder < 63:
        billettpris = 50
    else:
        billettpris = 35
    
    print("Hei" + navn + "Din billett koster" + billettpris)


RegnUtPris()
    