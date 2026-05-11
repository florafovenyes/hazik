szamok = [100, 200, 56, 80, 97, 4, 65, 88, 14, 22, 68]
paros = 0
paratlan = []

for szam in szamok:
    if szam % 2 == 0:
        paros += szam
    else:
        paratlan.append(szam)

print("A páros számok összege:", paros)
print("Páratlan számok:",paratlan)
