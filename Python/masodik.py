filename = 'ki.txt'

def is_number(szam):
    try:
        float(szam)
        return True
    except ValueError:
        return False


def rendez(line, csokkeno, algoritmus):
    if all(is_number(item) for item in line):  
        line = [int(item) for item in line]  
        key = lambda x: x
    else:
        key = lambda x: len(x)  

    if algoritmus == '1':  
        n = len(line)
        for i in range(n):
            minimum = i
            for j in range(i + 1, n):
                if (key(line[j]) < key(line[minimum]) and not csokkeno) or (key(line[j]) > key(line[minimum]) and csokkeno):
                    minimum = j
            line[i], line[minimum] = line[minimum], line[i]
    elif algoritmus == '2':  
        for i in range(1, len(line)):
            key_value = line[i]
            j = i - 1
            while j >= 0 and ((key(key_value) < key(line[j]) and not csokkeno) or (key(key_value) > key(line[j]) and csokkeno)):
                line[j + 1] = line[j]
                j -= 1
            line[j + 1] = key_value
    else:
        print("Hiba: Érvénytelen rendezési algoritmus.")
    return line

def menu():
    try:
        with open(filename, 'r') as file:
            lines = file.read().strip().splitlines()
        data = [line.split(';') for line in lines]
    except FileNotFoundError:
        print(f"Hiba: {filename} nem található.")
        data = None

    if data is None:
        quit()


    rendezi = input("Válaszd ki a rendezés irányát (n: növekvő, c: csökkenő): ")
    csokkeno = True if rendezi == 'c' else False


    print("Válaszd ki a rendezési algoritmust:")
    print("1. Egyszerű cserés rendezés")
    print("2. Beszúrásos rendezés")
    algoritmus = input("Add meg a választásodat (1 vagy 2): ")
    rendezett = [rendez(line, csokkeno, algoritmus) for line in data]
    print("Rendezett adatok:", rendezett)


    try:
        with open(filename, 'w') as file:
            for line in rendezett:
                file.write(';'.join(map(str, line)) + '\n')
    except Exception as e:
        print(f"Hiba történt a fájl írása közben: {e}")

    ok = True
    while ok:
        sor_index = int(input("Melyik sorba szeretnéd az új számot vagy szót beilleszteni? (1-től kezdve, vagy írj 'kilépés'-t a befejezéshez): ") or "-1") - 1
        if sor_index < 0 or sor_index >= len(rendezett):
            print("Hiba: Érvénytelen sorindex.")
            continue

        new_elem = input("Adj meg egy új számot vagy szót: ")
        if is_number(new_elem):
            new_elem = int(new_elem)

        rendezett[sor_index].append(new_elem)
        rendezett[sor_index] = rendez(rendezett[sor_index], csokkeno, algoritmus)

        print("Frissített rendezett adatok:", rendezett)


        try:
            with open(filename, 'w') as file:
                for line in rendezett:
                    file.write(';'.join(map(str, line)) + '\n')
        except Exception as e:
            print(f"Hiba történt a fájl írása közben: {e}")

menu()