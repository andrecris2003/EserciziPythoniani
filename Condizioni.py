#Condizioni
import random

print("Esercizio condizioni(if,else,elif)")
print("RANDOMLE\ntrovail numero generato random da 1 a 100")
numran=random.randint(1,100)
try:
    n1=int(input("Inserisci il primo numero"))
except ValueError:
    n1=0
if n1==numran:
    print("Hai vinto.")
elif n1<numran:
    print("Hai scelto un numero troppo piccolo.")
else:
    print("Hai scelto un numero troppo grande.")  
print(f"Il numero random era {numran}")