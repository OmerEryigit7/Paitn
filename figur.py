svar = ""

class figure:
    def __init__(self, length = None, height = None, radius = None):
        self.length = length
        self.height = height
        self.radius = radius

class circle(figure):
    def __init__(self, radius):
        super().__init__(radius=radius)
        print(3.14 * self.radius * self.radius)


class rectangle(figure):
    def __init__(self, length, height):
        super().__init__(length=length, height=height)
        print(self.height*self.length)

print("hva vil du regne ut? S for sirkel, R for rektangel og K for kvadrat")
method = input().upper()

if method == "S" or "SIRKEL": 
    print("Skriv inn radius")
    circle(int(input()))

elif method == "R" or "REKTANGEL" or "K" or "KVADRAT":
    length = input("Skriv inn lengden")
    height = input("Skriv inn høyden")
    rectangle(int(input(length, height)))


#circle(4)
#rectangle(3, 4)

