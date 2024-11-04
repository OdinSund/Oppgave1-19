liste = []

tall = 1
while tall != 0:
    tall = int(input("Skriv et tall: "))
    liste.append(tall)

for i in liste:
    print(i)
    i + 1

minSum = 0

for i in liste:
    minSum += i
    i + 1

print(minSum)

maxnum = 0
for i in liste:
    if i > maxnum:
        maxnum = i
    
print(maxnum)
    
minnum = maxnum
for i in liste:
    if i < minnum:
        minnum = i

print(minnum)
