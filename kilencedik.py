class Konyv:
    def __init__(self, cim, szerzo):
        self.cim = cim
        self.szerzo = szerzo

    def __str__(self):
        return f"{self.cim} - {self.szerzo}"

class Konyvtar:

    def __init__(self):
        self.konyvek = []

    def hozzad(self, konyv):
        self.konyvek.append(konyv)

    def listaz(self):
        print("Lista:")
        for konyv in self.konyvek:
            print(konyv)

    def __str__(self):
        # Ugyanaz a tartalom, mint listaz(), de stringként visszaadva
        if not self.konyvek:
            return "Lista:"  # Ha üres, csak a fejléc
        result = "Lista:\n"
        result += "\n".join(str(konyv) for konyv in self.konyvek)
        return result

konyvtar = Konyvtar()
konyvtar.hozzad(Konyv("Egri csillagok", "Gárdonyi Géza"))
konyvtar.hozzad(Konyv("1984", "George Orwell"))

# Csak egyszer írja ki (ugyanaz, mint listaz(), de egyszerűbben):
print(konyvtar)