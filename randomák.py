import random

def main():
    staty = ['Česká republika', 'Slovensko', 'Německo', 'Francie', 'Spojené státy', 'Spojené království', 'Rusko', 'Kanada', 'Austrálie', 'Japonsko']
    spravny_stat = random.choice(staty)
    pokusy = 0

    print("Hádej, o který stát se jedná.")

    while True:
        hadany_stat = input("Hádej stát: ")
        pokusy += 1

        if hadany_stat.lower() == spravny_stat.lower():
            print(f"Gratuluji, uhádl jsi stát {spravny_stat}!")
            print(f"Počet pokusů: {pokusy}")
            break
        else:
            print("Špatně, zkuste to znovu.")

if __name__ == "__main__":
    main()