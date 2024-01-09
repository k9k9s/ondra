import random
from colorama import init, Fore, Style
init()

mistnosti = ["obývák", "chodba", "sklep", "trůnní sál"]


chodby = [[1, 2], [0], [0], [1, 2]]
zamcene_chodby = [[], [3], [], []]
klic = 2

zlato = [1, 0, 10, 300]

hrac = 0
skore = 0
kroky = 0
ma_klic = False

def hotovo():
    return sum(zlato) == 0

while not hotovo():
    print("hráč je v místnosti:", mistnosti[hrac])
    print("hráč má", skore, "zlata")
    print("zbývá zlata:", sum(zlato))
    if random.random()<0.2:
        print(Fore.RED + "pozor padá meteorit")
        print(Style.RESET_ALL)



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














