#Cicli
import random
import time

print("Esercizio cicli(while,for)")
print("RANDOMLE\ntrovail numero generato random da 1 a 100")
win=False
numran=random.randint(1,100)
while not win: 
    try:
        n1=int(input("Inserisci numero\n"))
    except ValueError:
        n1=0
    if n1==numran:
        print("Hai vinto.")
        win=True
    elif n1<numran:
        print("Hai scelto un numero troppo piccolo.")
    else:
        print("Hai scelto un numero troppo grande.")
print(f"Il numero random era {numran}")
y=10
for i in range(0,11):
    print(f"Chiusura del programma in {y}...")
    y-=1
    time.sleep(1)
