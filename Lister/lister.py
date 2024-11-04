import math

tall = [1, 2, 3]
tall.append(4)
print(tall[0], tall[2])

print(sum(tall))
print(math.prod(tall))

tall2 = [sum(tall), math.prod(tall)]

tall3 = [tall, tall2]
print(tall3)
print(tall3.pop(1))
print(tall3)

tall4 = []
for i in range(4):
    tall4.append(input("Skriv inn et navn: "))

mittnavn = "Odin"

if mittnavn in tall4:
    print("Du husket meg!")
else:
    print("Glemte du meg?")