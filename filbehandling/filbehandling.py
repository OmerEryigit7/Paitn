x = ""

path = "/home/elev/Documents/Paitn/filbehandling/tekst.txt"

def lese():
    x = open(path, "r")
    print(x.read())

def overwrite():
    x = open(path , "w")
    x.write(detdunettopskrevinnpåterminalen)

def skrive():
    x = open(path, "a")
    x.write(detdunettopskrevinnpåterminalen)

def søke(ord):
    with open(path, "r") as fil:
        for linje in fil:
            if ord in linje:
                print(linje)

def slåsammen():
    with open(fil1 and fil2, "r") as fil:
        x = open(fil3, "a")
        for linje in fil:
            x.write(linje)
            

    #x = open(fil2, "")

choice = input("Hva vil du gjøre?")

if choice == "lese":
    lese()

elif choice == "slette og skrive":
    detdunettopskrevinnpåterminalen = input()
    overwrite()

elif choice == "skrive":
    detdunettopskrevinnpåterminalen = input()
    skrive()

elif choice == "søke":
    print("Hvilket ord/setning vil du søke etter?")
    detdunettopskrevinnpåterminalen = input()
    søke(detdunettopskrevinnpåterminalen)

elif choice == "slå sammen":
    fil1 = input("Hvor ligger fil 1?")
    fil2 = input("Hvor ligger fil 2?")
    fil3 = input("Hvor ligger fil 3?")
    slåsammen()

x = open(path, "r")
lines = x.readlines()
lines = len(lines)
lines = str(lines)
print("Det er "+lines+" linjer med tekst")
