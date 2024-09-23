import random
import string

# 1. Véletlen egész számok generálása
def veletlen_szamok_generalo(darabszam, minimum, maximum):
    return [random.randint(minimum, maximum) for _ in range(darabszam)]

# 2. Véletlen szövegek generálása
def veletlen_szoveg_generalo(darabszam):
    szovegek = []
    for _ in range(darabszam):
        hossz = random.randint(1, 20)  # Szöveg hossza véletlen 1 és 20 között
        szoveg = ''.join(random.choice(string.ascii_letters) for _ in range(hossz))
        szovegek.append(szoveg)
    return szovegek

# Menü funkció
def menu():
    while True:
        print("Válassz egy lehetőséget:")
        print("1. Véletlen egész számok generálása")
        print("2. Véletlen szövegek generálása")
        print("3. Kilépés")
        
        valasztas = input("Írd be a választott lehetőség számát (1-3): ")
        
        if valasztas == '1':
            # Véletlen egész számok generálása
            darabszam = int(input("Hány véletlen egész számot szeretnél generálni? "))
            minimum = int(input("Add meg a minimum értéket: "))
            maximum = int(input("Add meg a maximum értéket: "))
            
            veletlen_szamok = veletlen_szamok_generalo(darabszam, minimum, maximum)
            
            # Eredmények kiírása fájlba, fejléc hozzáadásával
            with open("ki.txt", "a") as file:  # 'a' mód az append, nem felülír
                file.write("Veletlen szamok:\n")
                file.write(";".join(map(str, veletlen_szamok)) + "\n")
            print("Eredmények a 'ki.txt' fájlba írva.")
        
        elif valasztas == '2':
            # Véletlen szövegek generálása
            darabszam = int(input("Hány véletlen szöveget szeretnél generálni? "))
            
            veletlen_szovegek = veletlen_szoveg_generalo(darabszam)
            
            # Eredmények kiírása fájlba, fejléc hozzáadásával
            with open("ki.txt", "a") as file:  # 'a' mód az append, nem felülír
                file.write("Veletlen szovegek:\n")
                file.write(";".join(veletlen_szovegek) + "\n")
            print("Eredmények a 'ki.txt' fájlba írva.")
        
        elif valasztas == '3':
            print("Kilépés...")
            break
        
        else:
            print("Érvénytelen választás! Próbáld újra.")

# Főprogram futtatása
menu()
