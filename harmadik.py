def feladat3():
    """3. feladat: 	Olvasd be a fájlt, tárold a sorokat listában, majd írd ki a lista tartalmát egy sorként egy másik fájlba!"""

    # beolvasás
    # üres lista
    lista=[]
    beFajl = open('dal.txt', 'r', encoding="utf-8")
    for sor in beFajl:
        lista.append(sor.strip())
        # print(sor.strip(), end="")

    # fájl bezárása
    beFajl.close()

    #programozós ellenőrzés
    # print(lista)
    # kiírása egy másik fájlba
    kiFajl = open("harmadikKi.txt","a", encoding="utf-8")
    for sor in lista:
        kiFajl.write(sor)
    kiFajl.close()