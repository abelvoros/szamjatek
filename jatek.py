import random
import time

print("Szamjatek")
name=input("Neved?\n")
print("Szervusz {}!".format(name))
print("Jatekszabaly: Gondolok egy szamra 1-tol 100-ig, talald ki!")
x=input("Van-e kedved jatszani? [y/n]: ")
if x!="y":
  print("Viszlat {}!".format(name))
  exit(0)

print("Jatek kezdodik")

random.seed(time.time())
number=random.randint(1, 100)
tip=0
count=1
while tip!=number:
  tip_str=input("Tippelj! ")
  tip=int(tip_str)
  if tip>number:
    print("Kisebb...")
    count+=1
  elif tip<number:
    print("Nagyobb...")
    count+=1
print("Eltalaltad {}, a szam valoban {} volt! {} tippbol talaltad el".format(name,number,count))

