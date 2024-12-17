def feladatNyolc():
    """8. feladat: 	Az K és az k betűt a cenzúra betiltotta. Írd ki a szöveget úgy, hogy helyettük csillagot írsz! A végére írd ki, hogy hány K és hány k betűt helyettesítettél csillaggal!"""
    dbk = 0
    dbK = 0
    beFajl = open("dal.txt", "r", encoding="utf-8")
    for sor in beFajl:
       for betu in sor:
           if betu == "k":
               dbk +=1
               print("*", end="")
           elif betu == "K":
               dbK +=1
               print("*", end="")
           else:
               print(betu, end="")
       #print("\n")
    beFajl.close()
    print("K betűk száma: "+str(dbK)+", k betűk száma: "+str(dbk))
