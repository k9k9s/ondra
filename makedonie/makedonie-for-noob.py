import random
from colorama import init, Fore, Style
init()

mistnosti_co_hoří = []
kam_lze_jit_a_hori = []
mistnosti = ["0-obývák", "1-chodba", "2-sklep", "3-trůnní sál", "4-jídelna","5-terasa","6-půda","7-kumbál"]
chodby = [[1, 2,4], [0,4,6], [0], [1, 2],[1,0,5,7],[4,6],[1,5],[4]]
zamcene_chodby = [[], [3], [], [],[],[],[],[]]
inventar = {"klic" : False, "moje zlato":0,"burger":False,"hasicak":False,}
cena_burgeru=15
sytost=4
mistnost_s_klicem = random.choice([2,6,7])
mistnost_s_hasicakem = 2
mistnost_s_pasti = random.choice([7])
zlato = [1, 0, 10, 50,15,20,4,0]
hrac = 0
skore = 0
kroky = 0
prisera = None








def prunik(seznam1, seznam2):
    return list(set(seznam1) & set(seznam2))
def je_cislo(mozna_cislo):
    try:
        int(mozna_cislo)
        return True
    except ValueError:
        return False
def hotovo():
    return sum(zlato) == 0




while not hotovo():
    # diagnostika
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
    print("mas kroky", [kroky])
    if hrac in mistnosti_co_hoří:
        print(Fore.RED + "bůh vám vskazuje že jste uhořel")
    if prisera is not None:
        print(Fore.YELLOW + "prisera je v mistnosti " + mistnosti[prisera])
        print(Style.RESET_ALL)
    print("hráč je v místnosti:", mistnosti[hrac])
    print("hráč má", skore, "zlata")
    print("zbývá zlata:", sum(zlato))
    kam_lze_jit = chodby[hrac]
    pada_meteorit = False
    if random.random() < 0.2 and hrac != 2 and kroky > 4:
        print(Fore.RED + "pozor padá meteorit")
        print(Style.RESET_ALL)
        pada_meteorit = True
    if random.random() < 0.5 and hrac == mistnost_s_pasti and prisera is None:
        print(Fore.RED + "šlápl jsi na past a vypustil jsi priseru")
        print(Style.RESET_ALL)
        prisera = 2



    kam_lze_jit_a_hori = prunik(kam_lze_jit, mistnosti_co_hoří)




    # moznosti
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
    if not (kam_lze_jit_a_hori == []) and inventar["hasicak"]:
        print("moznost U : uhasit mistnosti kolem co hoří")
    if not (kam_lze_jit_a_hori == [] ):
        print(Fore.YELLOW + "pozor můžeš jít do místnosti co hoří", kam_lze_jit_a_hori)
        print(Style.RESET_ALL)





    #kontrola
    vstup_ok=False
    while not vstup_ok:
        vstup = input("> ")
        if not inventar["klic"] and mistnost_s_klicem==hrac and vstup=="c" :
            vstup_ok=True
        elif not inventar["hasicak"]  and mistnost_s_hasicakem==hrac and vstup=="h":
            vstup_ok=True
        elif zlato[hrac] and vstup=="x":
            vstup_ok = True
        elif vstup=="u" and inventar["hasicak"]:
            vstup_ok=True
        elif (hrac==4 or inventar["burger"]) and vstup=="j" :
            vstup_ok=True
        elif vstup=="r" and hrac==1 and zamcene_chodby[hrac]:
            vstup_ok=True
        elif hrac == 4 and inventar["moje zlato"] >= cena_burgeru and not inventar["burger"] and vstup=="b":
            vstup_ok=True
        elif je_cislo(vstup) and int(vstup) <= len(kam_lze_jit) and int(vstup) > 0 :
            vstup_ok=True




    #vyhodnocovani
    if pada_meteorit and vstup in ["x" , "k"  , "j" ,"b" , "r", "h", "u","i","c","a","z","g"]:
        print(Fore.RED + "bůh vám skazuje že jte umřel při tragické nehodě pádu meteoritu")
        print(Style.RESET_ALL)
        break
    if pada_meteorit and vstup in ["1" , "2"  , "3" ,"4","5","6"]:
        mistnosti_co_hoří.append(hrac)
    if vstup == "x":
        skore += zlato[hrac]
        inventar["moje zlato"]+=zlato[hrac]
        zlato[hrac] = 0
    elif vstup == "u":
        mistnosti_co_hoří = []
        kam_lze_jit_a_hoři = []
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
        mistnost_s_hasicakem = -1
    elif vstup == "r":
        cilova_mistnost = zamcene_chodby[hrac].pop()
        chodby[hrac].append(cilova_mistnost)
        print("Slyšíš jak cvaknul zámek a dveře se otevřely.")

    else:
        hrac = kam_lze_jit[int(vstup) - 1]

    if hrac == prisera:
        print(Fore.RED + "bůh vám skazuje že si vás dala prisera ke svace")
        print(Style.RESET_ALL)
        break
    sytost-=1
    kroky += 1
    if sytost == 0:
        print(Fore.RED + "bůh vám skazuje že jte umřel hlady")
        print(Style.RESET_ALL)
        break
    if hrac in mistnosti_co_hoří:
        print(Fore.RED + "bůh vám vskazuje že jste uhořel")
        print(Style.RESET_ALL)
        break

    if prisera is not None:
        prisera = random.choice(chodby[prisera])


if sytost > 0:
    print(Fore.GREEN + "Gratuluju, sebral jsi celkem,", skore, "zlata za", kroky, "kroků")
    print(Style.RESET_ALL)