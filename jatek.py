import random

print("Szamjatek")
name=input("Neved?\n")
print("Szervusz {}!".format(name))
print("Jatekszabaly: Gondolok egy szamra 1-tol 100-ig, talald ki!")
x=input("Van-e kedved jatszani? [y/n]: ")
if x!="y":
  print("Viszlat {}!".format(name))
  exit(0)

print("Jatek kezdodik")

random.seed(1)
number=random.randint(1, 100)
tip=0
while tip!=number:
  tip_str=input("Tippelj! ")
  tip=int(tip_str)
  if tip>number:
    print("Kisebb...")
  elif tip<number:
    print("Nagyobb...")
print("Eltalaltad {}, a szam valoban {} volt!".format(name,number))

