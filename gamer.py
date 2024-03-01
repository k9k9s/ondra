import random
from colorama import init, Fore, Style
init()

mistnosti_co_hoří = []
mistnosti = ["obývák", "chodba", "sklep", "trůnní sál","jídelna","terasa"]
chodby = [[1, 2,4], [0,4], [0], [1, 2],[1,0,5],[4]]
zamcene_chodby = [[], [3], [], [],[],[]]
inventar = {"klic" : False, "moje zlato":0,"burger":False,"hasicak":False}
cena_burgeru=15
sytost=4
mistnost_s_klicem = 5
mistnost_s_hasicakem = 2
zlato = [1, 0, 10, 300,15,20]
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

    if sytost == 2:
        print(Fore.RED + "pozor na sytost")
        print(Style.RESET_ALL)

    if sytost == 1:
        print(Fore.RED + "pozor na sytost")
        print(Style.RESET_ALL)

    if inventar["burger"]:
        print("mas burger")

    if inventar["klic"]:
        print("mas klíč")

    if inventar["hasicak"]:
        print("mas hasičák")

    print(mistnosti_co_hoří)

    if hrac in mistnosti_co_hoří:
        print(Fore.RED + "bůh vám vskazuje že jste uhořel")
        print(Style.RESET_ALL)
        break




    print("hráč je v místnosti:", mistnosti[hrac])
    print("hráč má", skore, "zlata")
    print("zbývá zlata:", sum(zlato))
    kam_lze_jit = chodby[hrac]

    pada_meteorit = False
    if random.random() < 1.0 and hrac != 2 and kroky > 2:
        print(Fore.RED + "pozor padá meteorit")
        print(Style.RESET_ALL)
        pada_meteorit = True



    for i, moznost in enumerate(kam_lze_jit):
        print("Moznost", i + 1, ": ", mistnosti[moznost])
    if zlato[hrac] > 0:
        print("Moznost X : sebrat", zlato[hrac], "zlata")
    if hrac == mistnost_s_klicem:
        print("Moznost C : sebrat klíč")
    if hrac == mistnost_s_hasicakem:
        print("Moznost H : sebrat hasicak")
    if inventar["klic"] and zamcene_chodby[hrac]:
        print("Moznost R : odemknout dveře ->", mistnosti[zamcene_chodby[hrac][-1]])
    if hrac == 4 or inventar["burger"]:
        print("moznost J: najíst se")
    if hrac == 4 and inventar["moje zlato"] >= cena_burgeru:
        print("prodavačka říká:Chceš burger?řekni b")

    vstup_ok=False
    while not vstup_ok:
        vstup = input("> ")
        if not inventar["klic"] and mistnost_s_klicem==hrac and vstup=="c":
            vstup_ok=True
        if not inventar["hasicak"] and mistnost_s_hasicakem==hrac and vstup=="h":
            vstup_ok=True
        elif zlato[hrac] and vstup=="x":
            vstup_ok=True
        elif (hrac==4 or inventar["burger"]) and vstup=="j":
            vstup_ok=True
        elif vstup=="r" and hrac==1 and zamcene_chodby[hrac]:
            vstup_ok=True
        elif hrac == 4 and inventar["moje zlato"] >= cena_burgeru and not inventar["burger"] and vstup=="b":
            vstup_ok=True
        elif je_cislo(vstup) and int(vstup) <= len(kam_lze_jit) and int(vstup) > 0:
            vstup_ok=True

    if pada_meteorit and vstup in ["x" , "k"  , "j" ,"b" , "r", "h"]:
        print(Fore.RED + "bůh vám skazuje že jte umřel při tragické nehodě pádu meteoritu")
        print(Style.RESET_ALL)
        break

    if pada_meteorit and vstup in ["1" , "2"  , "3" ,"4"]:
        mistnosti_co_hoří.append(hrac)












    if vstup == "x":
        skore += zlato[hrac]
        inventar["moje zlato"]+=zlato[hrac]
        zlato[hrac] = 0
    elif vstup == "c":
        inventar["klic"] = True
        mistnost_s_klicem = -1
    elif vstup=="j":
        sytost=11
        if not hrac==4:
            inventar["burger"]=False
    elif vstup == "b":
        inventar["burger"]=True
    elif vstup == "h":
        inventar["hasicak"] = True
        mistnost_s_klicem = -1

    elif vstup == "r":
        cilova_mistnost = zamcene_chodby[hrac].pop()
        chodby[hrac].append(cilova_mistnost)
        print("Slyšíš jak cvaknul zámek a dveře se otevřely.")
    else:
        hrac = kam_lze_jit[int(vstup) - 1]




    sytost-=1
    kroky += 1
    if sytost == 0:
        print(Fore.RED + "bůh vám skazuje že jte umřel hlady")
        print(Style.RESET_ALL)
        break
if sytost > 0:
    print(Fore.GREEN + "Gratuluju, sebral jsi celkem,", skore, "zlata za", kroky, "kroků")
    print(Style.RESET_ALL)
