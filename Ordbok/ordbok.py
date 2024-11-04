Dict = {"melk": 14.90, "brød": 24.90, "yoghurt": 12.90, "pizza":39.90}
print(Dict)


for i in range(2):
    nøkkel = input("Skriv inn en matvare: ")
    verdi = input("Skriv inn prisen på denne varen i kroner: ")
    Dict[nøkkel] = float(verdi)

print(Dict)