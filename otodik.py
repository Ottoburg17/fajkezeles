def feladat5():
    """5. feladat: 	Olvasd be a fájlt, és írd ki a tartalmát egy másik fájlba, úgy, hogy nem tárolod el a szöveget, hanem minden sort azonnal kiírsz!"""
    kiFajl = open("otodikKi.txt", "w", encoding="utf-8")
    beFajl = open("dal.txt", "r", encoding="utf-8")
    for sor in beFajl:
        kiFajl.write(sor)
    beFajl.close()
    kiFajl.close()