def feladat4():
    """4. feladat: 	Olvasd be a fájlt, tárold a sorokat listában, majd írd ki a lista tartalmát így, ahogy beolvastad, soronként egy szóval egy másik fájlba!"""

    dalSorok=[]
    beFajl = open("dal.txt", "r", encoding="utf-8")
    for sor in beFajl:
        dalSorok.append(sor.strip())
    beFajl.close()

    kiFajl = open("negyedikKi.txt", "w", encoding="utf-8")
    for sor in dalSorok:
        szavak =sor.split(" ")
        kiFajl.write(szavak[0])
        kiFajl.write("\n")
    kiFajl.close()


