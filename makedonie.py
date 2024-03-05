 vstup_ok=True
        elif je_cislo(vstup) and int(vstup) <= len(kam_lze_jit) and int(vstup) > 0:
            vstup_ok=True

    #vyhodnocovani
    if pada_meteorit and vstup in ["x" , "k"  , "j" ,"b" , "r", "h", "u"]:
        print(Fore.RED + "bůh vám skazuje že jte umřel při tragické nehodě pádu meteoritu")
        print(Style.RESET_ALL)
@@ -136,16 +153,25 @@ def hotovo():
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
