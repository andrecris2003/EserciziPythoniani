import math
import random
s=1
while s!=0:
    print("CALCOLATRICE")
    while s==-1:
        try:
            s=int(input("Inserisci operazione da svolgere\n0) Esci\n1) Somma\n2) Sottrazione\n3) Moltiplicazione\n4) Divisione\n5) Potenza\n6) Radice quadrata\n7) Logaritmo naturale\n8) Maggiore\n9) Minore\n10) Uguale"))
        except ValueError:
            s=-1
    if isinstance(s, int):
        if s==0 :
            print("Chiusura programma")
        elif s==1 :
            print("HAI SCELTO SOMMA")
            n1=int(input("Inserisci il primo numero"))
            n2=int(input("Inserisci il secondo numero"))
            print(f"La somma dei 2 numeri è: {n1+n2}")
        elif s==2 :
            print("HAI SCELTO SOTTRAZIONE")
            n1=int(input("Inserisci il primo numero"))
            n2=int(input("Inserisci il secondo numero"))
            print(f"La sotrazione dei 2 numeri è: {n1-n2}")
        elif s==3 :
            print("HAI SCELTO MOLTIPLICAZIONE")
            n1=int(input("Inserisci il primo numero"))
            n2=int(input("Inserisci il secondo numero"))
            print(f"La moltiplicazione dei 2 numeri è: {n1*n2}")
        elif s==4 :
            print("HAI SCELTO DIVISIONE")
            n1=int(input("Inserisci il primo numero"))
            n2=int(input("Inserisci il secondo numero"))
            if n2!=0 :
                print(f"La divisione dei 2 numeri è: {float(n1/n2)}")
            else : 
                print("Impossibile")
        elif s==5 :
            print("HAI SCELTO POTENZA")
            n1=int(input("Inserisci il primo numero"))
            n2=int(input("Inserisci il secondo numero"))
            print(f"La potenza del primo numero elevato al secondo è: {n1**n2}")
        elif s==6 :
            print("HAI SCELTO RADICE QUADRATA")
            n1=int(input("Inserisci il primo numero"))
            print(f"La radice quadrata del numero è: {math.sqrt(n1)}")
        elif s==7 :
            print("HAI SCELTO LOGARITMO NATURALE")
            n1=int(input("Inserisci il primo numero"))
            print(f"Il logartmo naturale del numero è: {round(math.log(float(n1)),2)}")
        elif s==8 :
            print("HAI SCELTO MAGGIORE")
            n1=int(input("Inserisci il primo numero"))
            n2=int(input("Inserisci il secondo numero"))
            if n1>n2 :
                print(f"{n1} è maggiore di {n2}")
            else : 
                print(f"{n1} non è maggiore di {n2}")
        elif s==9 :
            print("HAI SCELTO MINORE")
            n1=int(input("Inserisci il primo numero"))
            n2=int(input("Inserisci il secondo numero"))
            if n1<n2 :
                print(f"{n1} è minore di {n2}")
            else : 
                print(f"{n1} non è minore di {n2}")
        elif s==10 :
            print("HAI SCELTO UGUALE")
            n1=int(input("Inserisci il primo numero"))
            n2=int(input("Inserisci il secondo numero"))
            if n1==n2 :
                print(f"{n1} è uguale di {n2}")
            else : 
                print(f"{n1} non è uguale a {n2}")
        else:
            print("SEI UN COGLIONE")
"""
insulti = ["vaffanculo","coglione","merda","grullo","frocio","negro","pervertito","gay","deficente","cazzo"]
insulto = input("Quale insulto vuoi cercare?").lower()
if insulto in insulti:
    print(f"L'insulto {insulto} è presente nella lista")
else:
    print(f"L'insulto {insulto} non è presente nella lista")
"""