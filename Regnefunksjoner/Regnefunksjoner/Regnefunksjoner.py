tall1 = 1
tall2 = 1
tall3 = 1

def addisjon(num1, num2):
    return num1 + num2

def subtraksjon(num1, num2):
    return num1 - num2

def divisjon(num1, num2):
    return num1 / num2

def tommerTilCm(antallTommer):
    return antallTommer * 2.54

def skrivBeregninger():
    global tall1
    tall1 = int(input("Skriv inn ett tall: "))
    
    global tall2
    tall2 = int(input("Skriv inn ett tall: "))
    
    global tall3
    tall3 = int(input("Skriv inn ett tall: "))
    
    
    
       
skrivBeregninger()
print(addisjon(tall1, tall2))
print(subtraksjon(tall1, tall2))  
print(divisjon(tall1, tall2))
print(tommerTilCm(tall3))
