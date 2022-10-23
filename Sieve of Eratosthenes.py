import time

def eliminaMultipli(num):
  for x in numeri[numeri.index(num):]:
    if x==num:
      print("Nuovo numero primo trovato: "+str(x))
      continue
    if num>(num_max/2):
      return
    if x%num==0:
      numeri.remove(x)

num_max=123456
numeri=[]

start_time=time.time()

for x in range(num_max-1):
  numeri.append(x+2)

for numero in numeri:
  eliminaMultipli(numero)

print(numeri)

print("\nTotale numeri primi trovati: "+str(len(numeri)))

print("Tempo di esecuzione: "+str(time.time()-start_time)+" secondi")