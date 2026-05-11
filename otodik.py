def feldolgozas(kerdes):
    if(kerdes.endswith("?")):
        print("Ez bizony egy kérdés.")

    szamjegyek = dict()
    szamjegy_volt = False

    for betu in kerdes:
        if betu in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
            szamjegy_volt = True
            if betu in szamjegyek:
                szamjegyek[betu] += 1
            else:
                szamjegyek[betu] = 1

    if not szamjegy_volt:
        print("Ebben egy számjegy sem volt.")
    pontok_szama = kerdes.count(".")
    print("A kérdés " + str(pontok_szama) + " darab pontot tartalmaz")
    return szamjegyek

while True:
    kerdes = input("Kerdes : ")

    if kerdes == "exit" or kerdes == "quite":
        print("Bye!")
        break


    print("Ezt kerdezte: " + kerdes)

    valasz = feldolgozas(kerdes)

    print("Válasz: " + str(valasz))

print("VEGE.")