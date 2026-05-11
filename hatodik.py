katalogus = (
    {"szerzo": "Ernest Hemingway", "cim": "Az öreg halász és a tenger", "kiadas": 1952},
    {"szerzo": "Lev Tolsztoj", "cim": "Háború és béke", "kiadas": 1869},
    {"szerzo": "William Golding", "cim": "Legyek ura", "kiadas": 1954},
    {"forras": "ceges könyvtár", "katalogus": (
        {"szerzo": "Giovanni Boccaccio", "cim": "Dekameron", "kiadas": 1353},
        {"szerzo": "Miguel de Cervantes", "cim": "Don Quijote", "kiadas": 1605},
        {"szerzo": "Umberto Eco", "cim": "A rózsa neve", "kiadas": 1980},
        {"szerzo": "Gabriel García Márquez", "cim": "Száz év magány", "kiadas": 1967},
        {"szerzo": "Thomas Mann", "cim": "A varázshegy", "kiadas": 1924},
        {"szerzo": "Bulgakov Mihail", "cim": "A Mester és Margarita", "kiadas": 1967},
    )},
    {"szerzo": "Robert Merle", "cim": "Malevil", "kiadas": 1972},
    {"szerzo": "Philip K. Dick", "cim": "VALIS", "kiadas": 1981},
    {"szerzo": "Philip K. Dick", "cim": "Kamera által homályosan", "kiadas": 1977},
    {"szerzo": "Albert Camus", "cim": "A pestis", "kiadas": 1947},
    {"szerzo": "Joseph Conrad", "cim": "A sötétség mélyén", "kiadas": 1899},
    {"szerzo": "Cormac McCarthy", "cim": "Az út", "kiadas": 2006},
    {"szerzo": "Joseph Heller", "cim": "Valami történt", "kiadas": 1974},
    {"szerzo": "Milan Kundera", "cim": "A lét elviselhetetlen könnyűsége", "kiadas": 1984},
    {"forras" : "fiókkönyvtár", "katalogus": (
        {"szerzo": "Franz Kafka", "cim": "A per", "kiadas": 1925},
        {"szerzo": "Hermann Hesse", "cim": "Sziddhárta", "kiadas": 1922},
        {"szerzo": "Fyodor Dosztojevszkij", "cim": "Bűn és bűnhődés", "kiadas": 1866},
        {"szerzo": "Fyodor Dosztojevszkij", "cim": "A Karamazov testvérek", "kiadas": 1880},
        {"forras": "magángyűjtemény", "katalogus": (
            {"szerzo": "Stanislaw Lem", "cim": "Solaris", "kiadas": 1961},
            {"szerzo": "Arthur C. Clarke", "cim": "2001: Űrodüsszeia", "kiadas": 1968},
            {"szerzo": "Ursula K. Le Guin", "cim": "A sötétség balkeze", "kiadas": 1969},
        )},
        {"szerzo": "Hermann Hesse", "cim": "A pusztai farkas", "kiadas": 1927}
    )},
    {"szerzo": "George Orwell", "cim": "1984", "kiadas": 1949},
    {"szerzo": "Aldous Huxley", "cim": "Szép új világ", "kiadas": 1932},
    {"szerzo": "Ray Bradbury", "cim": "Fahrenheit 451", "kiadas": 1953}
    )

#print(katalogus)


def keres(katalogus, szerzo=None, cim=None, kiadas=None, case_sensitive_search=True):
    talalatok = []
    for elem in katalogus:
        if "katalogus" in elem:
            eredmeny = keres(elem["katalogus"], szerzo, cim, kiadas, case_sensitive_search)
            talalatok.extend(eredmeny)
        elif "cim" in elem:
            # Ellenőrzés case-sensitive vagy nem
            cim_talalat = cim is None or (
                cim in elem["cim"] if case_sensitive_search else cim.lower() in elem["cim"].lower())
            szerzo_talalat = szerzo is None or (
                szerzo in elem["szerzo"] if case_sensitive_search else szerzo.lower() in elem["szerzo"].lower())
            kiadas_talalat = kiadas is None or (isinstance(kiadas, int) and kiadas == elem["kiadas"]) or (
                        isinstance(kiadas, tuple) and kiadas[0] <= elem["kiadas"] <= kiadas[1])

            if cim_talalat and szerzo_talalat and kiadas_talalat:
                talalatok.append(elem)

    return talalatok

print(keres(katalogus, cim="Le"))
print(keres(katalogus, cim="le", case_sensitive_search=True))
print(keres(katalogus, cim="le", case_sensitive_search=False))


