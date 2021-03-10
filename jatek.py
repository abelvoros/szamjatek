import random
import time

print("Számjáték")
name=input("Neved?\n")
print("Szervusz {}!".format(name))
print("Játékszabály: Gondolok egy számra 1-től 100-ig, találd ki!")
x=input("Van-e kedved játszani? [y/n]: ")
if x!="y":
  print("Viszlát {}!".format(name))
  exit(0)

print("Kezdjük a játékot!")

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
print("Eltaláltad {}, a szám valóban {} volt! {} tippből találtad el.".format(name,number,count))

