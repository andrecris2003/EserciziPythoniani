import random

def StampaCartaTua(carta):
   if carta==11:
         print("Hai pescato un Alfiere")
   elif carta==12:
         print("Hai pescato una regina")
   elif carta==13:
         print("Hai pescato un re")
   else:
      print("Hai pescato ",carta)
      
def StampaCartaBanco(carta):
   if carta==11:
         print("Il banco ha pescato un Alfiere")
   elif carta==12:
         print("Il banco ha pescato una regina")
   elif carta==13:
         print("Il banco ha pescato un re")
   else:
      print("Il banco ha pescato ",carta)

GamaEnd=False
numbanco1 = random.randint(1,13)
StampaCartaTua(numbanco1)
if(numbanco1>10):
   numbanco1=10
numbanco2 = random.randint(1,13)
StampaCartaTua(numbanco2)
if(numbanco2>10):
   numbanco2=10
numgiocatore1 = random.randint(1,13)
if(numgiocatore1>10):
   numgiocatore1=10
numgiocatore2 = random.randint(1,13)
if(numgiocatore2>10):
   numgiocatore2=10
ibanco=0
if numbanco1==1:
   sommabanco=11
   ibanco+=1
else:
   sommabanco=numbanco1
print(f"Carta 1 giocatore: {numgiocatore1}\n")
print(f"Carta 2 giocatore: {numgiocatore2}\n")
print(f"Carta 1 banco: {sommabanco}\n")
i=0
somma=0
if (numgiocatore1==1 or numgiocatore2==1) and (numgiocatore1+numgiocatore2<=11):
   somma=numgiocatore1+numgiocatore2+10
   i+=1
else:
   somma = numgiocatore1+numgiocatore2
print(f"La somma delle tue carte è {somma}")
controllo = ""
while controllo!="lascia":
   controllo = input("Cosa vuoi fare: Pesca o Lascia\n").lower()
   if controllo=="pesca":
      pesca = random.randint(1,13)
      StampaCartaTua(pesca)
      if pesca>10:
         pesca=10
      if (pesca+somma)<11 and (pesca==1):
           somma=pesca+somma+10
           i+=1
      else:
         if (somma+pesca>21) and (i>0):
            somma=somma+pesca-10
         else:
               somma=pesca+somma
      if somma>=21:
         controllo="lascia"
      print("La somma delle tue carte è ",somma)
if somma>21:
   print("Hai perso")
   GamaEnd=True
else:
   print(f"Carta 2 banco: {numbanco2}\n")
   sommabanco=numbanco1+numbanco2
   print("La seconda carta del banco è ",numbanco2)
   while sommabanco<17:
      pescabanco=random.randint(1,13)
      if pescabanco>10:
         pescabanco=10
      if ibanco>=1 and sommabanco>21:
         sommabanco-=10
         print("Somma carte banco: ",sommabanco)
      else:
         print("Somma carte banco: ",sommabanco)
         if sommabanco>21:
            print("Hai VINTO")
         else:
            if somma>sommabanco:
               print("Hai VINTO")
            elif somma==sommabanco:
               print("Pareggio")
            else:
               print("Hai Perso")
         GamaEnd=True
   
