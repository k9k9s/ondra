import random
from colorama import init, Fore, Style
init()
form inputimeout import inputimeout, timeoutOccured


mistnosti = ["obývák", "chodba", "sklep", "trůnní sál","jídelna"]
chodby = [[1, 2,4], [0,4], [0], [1, 2],[1,0]]
zamcene_chodby = [[], [3], [], [],[]]
inventar = {"klic" : False, "moje zlato":0,"burger":False}
cena_burgeru=15
sytost=4
mistnost_s_klicem = 2
zlato = [1, 0, 10, 300,15]
hrac = 0
skore = 0
kroky = 0

def je_cislo(mozna_cislo):
    try:
        int(mozna_cislo)
        return True
    except ValueError:
        return False

def hotovo():
    return sum(zlato) == 0

while not hotovo():
    print("mas sytost",sytost)
    if inventar["burger"]:
        print("mas burger")
    print("hráč je v místnosti:", mistnosti[hrac])
    print("hráč má", skore, "zlata")
    print("zbývá zlata:", sum(zlato))
    kam_lze_jit = chodby[hrac]

    pada_meteorit = False
    if random.random()<1 and hrac != 2 and kroky >2:
        print(Fore.RED + "pozor padá meteorit")
        print(Style.RESET_ALL)
        pada_meteorit = True






    kam_lze_jit = chodby[hrac]
    for i, moznost in enumerate(kam_lze_jit):
        print("Moznost", i + 1, ": ", mistnosti[moznost])

    if zlato[hrac] > 0:
        print("Moznost X : sebrat", zlato[hrac], "zlata")

    if hrac == klic:
        print("Moznost K: sebrat klíč")

    vstup = input("> ")
    # vstup_ok = False
    # while not vstup_ok:
    #     vstup = input("> ")
    #
    #     if vstup == "x" and zlato[hrac] > 0:
    #         vstup_ok = True
    #         break

    if pada_meteorit and vstup in ["x" , "k"]:
        print(Fore.RED + "bůh vám skazuje že jte umřel při tragické nehodě pádu meteoritu")
        print(Style.RESET_ALL)
        break

    if vstup == "x":
        skore += zlato[hrac]
        zlato[hrac] = 0
    elif vstup == "k":
        ma_klic = True
        klic = -1
    else:
        index_moznosti = int(vstup) - 1
        hrac = kam_lze_jit[index_moznosti]

    kroky += 1
    #break

print("Gratuluju, sebral jsi celkem,", skore, "zlata za", kroky, "kroků")















