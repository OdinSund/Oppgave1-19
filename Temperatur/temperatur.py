with open('temperatur.txt', 'r') as file:
    data = file.read()
print(data)

verdier = data.split()

temperaturer = [int(verdi) for verdi in verdier]

print(temperaturer)

def gjennomsnitt(liste):
    sum = 0

    for temp in liste:
        sum += temp
    
    gjennomsnitt = sum / len(liste)

    return gjennomsnitt

print(gjennomsnitt(temperaturer))