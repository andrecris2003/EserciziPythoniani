#Input

print("Esercizio input")
try:
    n1=int(input("Inserisci il primo numero\n"))
except ValueError:
    n1=0
try:
    n2=int(input("Inserisci il secondo numero\n"))
except ValueError:
    n2=0
print(f"Somma = {n1+n2}")