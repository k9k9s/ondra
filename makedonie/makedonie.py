import random
from colorama import init, Fore, Style
init()

mistnosti_co_hoří = []
kam_lze_jit_a_hori = []
mistnosti = [
            "0-obývák",
            "1-chodba",
            "2-sklep",
            "3-trůnní sál",
            "4-jídelna",
            "5-terasa",
            "6-půda",
            "7-kumbál",
            "8-sídlo",
            "9-ložnice",
            "10-chodba",
            "11-tajemna komnata"
            ]
chodby = [
            [1, 2, 4],      # "0-obývák"
            [0,4,6],        # "1-chodba"
            [0,11],         # "2-sklep"
            [1, 2],         # "3-trůnní sál"
            [1,0,5,7],      # "4-jídelna"
            [4,6,10],       # "5-terasa"
            [1,5],          # "6-půda"
            [4],            # "7-kumbál"
            [10],           # "8-sídlo"
            [10],           # "9-ložnice"
            [9,8,5],        # "10-chodba"
            [2]             # "11-tajemna komnata"
        ]
zamcene_chodby = [[], [3], [], [],[],[],[],[],[],[],[],[],[]]
inventar = {"klic": False,
            "moje zlato": 0,
            "burger": False,
            "hasicak": False,
            "hulka": False
            }
cena_burgeru=15
sytost=4
mistnost_s_klicem = random.choice([1,2,5,6,7,9,10])
mistnost_s_hasicakem = 2
mistnost_s_pasti = random.choice([1,7])
zlato = [1, 0, 10, 100, 15,20,3,0,50,30,0,10]
mistnost_s_hracem = 0
skore = 0
kroky = 0
prisera = None
mistnost_s_baziliskem = 11
mistnost_s_náhrdelnikem = random.choice([6,5])
mistnost_s_hulkou = random.choice([3])
mistnost_s_voldemortem = 8







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
    if inventar["hulka"]:
        print("mas hulku")
    print("mas kroky", [kroky])
    if mistnost_s_hracem in mistnosti_co_hoří:
        print(Fore.RED + "bůh vám vskazuje že jste uhořel")
    if prisera is not None:
        print(Fore.YELLOW + "prisera je v mistnosti " + mistnosti[prisera])
        print(Style.RESET_ALL)
    print("hráč je v místnosti:", mistnosti[mistnost_s_hracem])
    print("hráč má", skore, "zlata")
    print("zbývá zlata:", sum(zlato))
    kam_lze_jit = chodby[mistnost_s_hracem]
    pada_meteorit = False
    if random.random() < 0.2 and mistnost_s_hracem != 2 and kroky > 3:
        print(Fore.RED + "pozor padá meteorit")
        print(Style.RESET_ALL)
        pada_meteorit = True
    if random.random() < 0.75 and mistnost_s_hracem == mistnost_s_pasti and prisera is None:
        print(Fore.RED + "šlápl jsi na past a vypustil jsi priseru")
        print(Style.RESET_ALL)
        prisera = 2
    if mistnost_s_hracem == mistnost_s_voldemortem:
        print(Fore.RED + "pozor jsi v místnosti z voldemortem")
        print(Style.RESET_ALL)
    if mistnost_s_hracem == mistnost_s_baziliskem:
        print(Fore.RED + "pozor jsi v místnosti z baziliskem")
        print(Style.RESET_ALL)




    kam_lze_jit_a_hori = prunik(kam_lze_jit, mistnosti_co_hoří)




    # moznosti
    for i, moznost in enumerate(kam_lze_jit):
        print("Moznost", i + 1, ": ", mistnosti[moznost])
    if zlato[mistnost_s_hracem] > 0:
        print("Moznost X : sebrat", zlato[mistnost_s_hracem], "zlata")
    if mistnost_s_hracem == mistnost_s_klicem:
        print("Moznost C : sebrat klíč")
    if mistnost_s_hracem == mistnost_s_hasicakem:
        print("Moznost H : sebrat hasicak")
    if mistnost_s_hracem == mistnost_s_náhrdelnikem and inventar["hulka"]:
        print ("moznost Z : zničit nahrdelnik")
    if inventar["klic"] and zamcene_chodby[mistnost_s_hracem]:
        print("Moznost R : odemknout dveře ->", mistnosti[zamcene_chodby[mistnost_s_hracem][-1]])
    if mistnost_s_hracem == mistnost_s_voldemortem and inventar["hulka"] and mistnost_s_baziliskem == None and mistnost_s_náhrdelnikem == None:
        print("Moznost A : zabít voldemorta")
    if mistnost_s_hracem == mistnost_s_baziliskem and inventar["hulka"]:
        print("Moznost G : zabít baziliska")
    if mistnost_s_hracem == 4 or inventar["burger"]:
        print("moznost J: najíst se")
    if mistnost_s_hracem == 4 and inventar["moje zlato"] >= cena_burgeru:
        print("prodavačka říká:Chceš burger?řekni b")
    if mistnost_s_hracem == mistnost_s_hulkou:
        print("Moznost I : sebrat hulku")
    if not (kam_lze_jit_a_hori == []) and inventar["hasicak"]:
        print("moznost U : uhasit mistnosti kolem co hoří")
    if not (kam_lze_jit_a_hori == [] ):
        print(Fore.YELLOW + "pozor můžeš jít do místnosti co hoří", kam_lze_jit_a_hori)
        print(Style.RESET_ALL)





    #kontrola
    vstup_ok=False
    while not vstup_ok:
        vstup = input("> ")
        if not inventar["klic"] and mistnost_s_klicem==mistnost_s_hracem and vstup=="c" :
            vstup_ok=True
        elif not inventar["hasicak"]  and mistnost_s_hasicakem==mistnost_s_hracem and vstup=="h":
            vstup_ok=True
        elif zlato[mistnost_s_hracem] and vstup=="x":
            vstup_ok = True
        elif mistnost_s_hracem == mistnost_s_hulkou and vstup =="i":
            vstup_ok=True
        elif mistnost_s_hracem == mistnost_s_náhrdelnikem and inventar["hulka"] and vstup =="z":
            vstup_ok=True
        elif mistnost_s_hracem == mistnost_s_voldemortem and inventar["hulka"] and mistnost_s_baziliskem == None and mistnost_s_náhrdelnikem == None and vstup == "a":
            vstup_ok = True
        elif mistnost_s_hracem == mistnost_s_baziliskem and inventar["hulka"] and vstup == "g":
            vstup_ok = True
        elif vstup=="u" :
            vstup_ok=True
        elif (mistnost_s_hracem==4 or inventar["burger"]) and vstup=="j" :
            vstup_ok=True
        elif vstup=="r" and mistnost_s_hracem==1 and zamcene_chodby[mistnost_s_hracem]:
            vstup_ok=True
        elif mistnost_s_hracem == 4 and inventar["moje zlato"] >= cena_burgeru and not inventar["burger"] and vstup=="b":
            vstup_ok=True
        elif je_cislo(vstup) and int(vstup) <= len(kam_lze_jit) and int(vstup) > 0 :
            vstup_ok=True
        else:
            print(Fore.RED + "MAS SPATNY VSTUP")
            print(Style.RESET_ALL)




    #vyhodnocovani
    if pada_meteorit and vstup in ["x" , "k"  , "j" ,"b" , "r", "h", "u","i","c","a","z","g"]:
        print(Fore.RED + "bůh vám vzkazuje, že jste umřel při tragické nehodě pádu meteoritu")
        print(Style.RESET_ALL)
        break
    if pada_meteorit and vstup in ["1" , "2"  , "3" ,"4","5","6"]:
        mistnosti_co_hoří.append(mistnost_s_hracem)
    if vstup == "x":
        skore += zlato[mistnost_s_hracem]
        inventar["moje zlato"]+=zlato[mistnost_s_hracem]
        zlato[mistnost_s_hracem] = 0
    elif vstup == "u":
        mistnosti_co_hoří = []
        kam_lze_jit_a_hoři = []
    elif vstup == "a":
        mistnost_s_voldemortem = None
    elif vstup == "g":
        mistnost_s_baziliskem = None
    elif vstup == "c":
        inventar["klic"] = True
        mistnost_s_klicem = -1
    elif vstup == "z":
        mistnost_s_náhrdelnikem = None
    elif vstup=="j":
        sytost=11
        if not mistnost_s_hracem==4:
            inventar["burger"]=False
    elif vstup == "b":
        inventar["burger"]=True
    elif vstup == "h":
        inventar["hasicak"] = True
        mistnost_s_hasicakem = -1
    elif vstup == "i":
        inventar["hulka"] = True
        mistnost_s_hulkou = -1
    elif vstup == "r":
        cilova_mistnost = zamcene_chodby[mistnost_s_hracem].pop()
        chodby[mistnost_s_hracem].append(cilova_mistnost)
        print("Slyšíš jak cvaknul zámek a dveře se otevřely.")

    else:
        # tady se hrac pohne
        mistnost_s_hracem = kam_lze_jit[int(vstup) - 1]

    if mistnost_s_hracem == prisera:
        print(Fore.RED + "bůh vám vzkazuje, že si vás dala prisera ke svace")
        print(Style.RESET_ALL)
        break
    sytost -= 1
    kroky += 1
    if sytost == 0:
        print(Fore.RED + "bůh vám vzkazuje, že jste umřel hlady")
        print(Style.RESET_ALL)
        break
    if mistnost_s_hracem in mistnosti_co_hoří:
        print(Fore.RED + "bůh vám vzkazuje, že jste uhořel")
        print(Style.RESET_ALL)
        break
    if mistnost_s_hracem == mistnost_s_voldemortem and vstup in ["x", "k", "j", "b", "r", "h", "u", "i", "c", "z"]:
        print(Fore.RED + "Brumbál vám vzkazuje, že na vás byla uvrhnuta kledba AVADA KEDAVRA")
        print(Style.RESET_ALL)
        break
    if mistnost_s_hracem == mistnost_s_baziliskem and vstup in ["x", "k", "j", "b", "r", "h", "u", "i", "c", "z"]:
        print(Fore.RED + "Brumbál vám vzkazuje, že si vás dal bazilišek jako dezert")
        print(Style.RESET_ALL)
        break
    if prisera is not None:
        prisera = random.choice(chodby[prisera])


if sytost > 0:
    print(Fore.GREEN + "Gratuluju, sebral jsi celkem,", skore, "zlata za", kroky, "kroků")
    print(Style.RESET_ALL)