class Eloleny:
    def __init__(self, nev, eletkor):
        self.nev = nev
        self.eletkor = eletkor

    def __str__(self):
        return f"Név: {self.nev}, Életkor: {self.eletkor}"

class Noveny(Eloleny):
    def __init__(self, nev, eletkor, vizigeny):
        super().__init__(nev, eletkor)
        self.vizigeny = vizigeny

    def __str__(self):
        return super().__str__() + f", Vízigény: {self.vizigeny}"

class Allat(Eloleny):
    def __init__(self, nev, eletkor, labak_szama):
        super().__init__(nev, eletkor)
        self.labak_szama = labak_szama

    def __str__(self):
        return super().__str__() + f", Lábak száma: {self.labak_szama}"

class Gomba(Eloleny):
    def __init__(self, nev, eletkor, mergezo_e):
        super().__init__(nev, eletkor)
        self.mergezo_e = mergezo_e

    def __str__(self):
        return super().__str__() + f", Mérgező-e: {self.mergezo_e}"

# Példányosítás és kiíratás
noveny = Noveny("Rózsa", 2, "Magas")
allat = Allat("Kutya", 5, 4)
gomba = Gomba("Galóca", 1, True)

print("Növény:")
print(noveny)
print("\nÁllat:")
print(allat)
print("\nGomba:")
print(gomba)