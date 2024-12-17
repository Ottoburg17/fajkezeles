def feladat1():
    """1. feladat: 	Olvasd be a fájlt, és írd ki a tartalmát egy sorba, úgy, hogy nem tárolod el a szöveget, hanem minden sort azonnal kiírsz!"""

    # beolvasás
    beFajl = open('dal.txt', 'r', encoding="utf-8")
    for sor in beFajl:
        print(sor.strip(), end="")

    # fájl bezárása
    beFajl.close()
