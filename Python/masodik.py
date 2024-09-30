def read_file(filename):
    """Beolvassa a fájl sorait, és soronként listákká alakítja."""
    try:
        with open(filename, 'r') as file:
            lines = file.read().strip().splitlines()  # Soronként olvassa be a fájlt
        data = [line.split(';') for line in lines]  # Minden sort pontosvessző mentén feloszt
        return data
    except FileNotFoundError:
        print(f"Hiba: {filename} nem található.")
        return None

def write_file(filename, data):
    """Visszaírja a rendezett adatokat a fájlba soronként, pontosvesszővel elválasztva."""
    try:
        with open(filename, 'w') as file:
            for line in data:
                file.write(';'.join(map(str, line)) + '\n')  # Soronként írja vissza a fájlba
    except Exception as e:
        print(f"Hiba történt a fájl írása közben: {e}")

def selection_sort(arr, key=lambda x: x, reverse=False):
    """Egyszerű cserés rendezés egy adott kulcs szerint (pl. szám vagy hossz)"""
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if (key(arr[j]) < key(arr[min_index]) and not reverse) or (key(arr[j]) > key(arr[min_index]) and reverse):
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

def insertion_sort(arr, key=lambda x: x, reverse=False):
    """Beszúrásos rendezés egy adott kulcs szerint (pl. szám vagy hossz)"""
    for i in range(1, len(arr)):
        key_value = arr[i]
        j = i - 1
        while j >= 0 and ((key(key_value) < key(arr[j]) and not reverse) or (key(key_value) > key(arr[j]) and reverse)):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key_value
    return arr

def is_number(s):
    """Eldönti, hogy egy adott string szám-e."""
    try:
        float(s)  # Próbáljuk meg számmá alakítani
        return True
    except ValueError:
        return False

def process_line(line, reverse, algo_choice):
    """Feldolgoz egy sort, eldöntve, hogy számokat vagy szavakat tartalmaz, és rendezve őket."""
    if all(is_number(item) for item in line):  # Ha minden elem szám
        line = [int(item) for item in line]  # Átalakítjuk int-té
        key = lambda x: x  # Számok esetén a rendezési kulcs maga a szám
    else:
        key = lambda x: len(x)  # Szavak esetén a rendezési kulcs a szó hossza

    # Választott rendezési algoritmus alkalmazása
    if algo_choice == '1':
        return selection_sort(line, key=key, reverse=reverse)
    elif algo_choice == '2':
        return insertion_sort(line, key=key, reverse=reverse)
    else:
        print("Hiba: Érvénytelen rendezési algoritmus.")
        return line

def main():
    filename = 'ki.txt'
    data = read_file(filename)

    if data is None:
        return

    # Rendezés irányának kiválasztása
    reverse_choice = input("Válaszd ki a rendezés irányát (n: növekvő, c: csökkenő): ")
    reverse = True if reverse_choice == 'c' else False

    # Rendezési algoritmus kiválasztása
    print("Válaszd ki a rendezési algoritmust:")
    print("1. Egyszerű cserés rendezés")
    print("2. Beszúrásos rendezés")
    algo_choice = input("Add meg a választásodat (1 vagy 2): ")

    # Minden sort külön rendezünk szám vagy szó alapján
    sorted_data = [process_line(line, reverse, algo_choice) for line in data]
    print("Rendezett adatok:", sorted_data)

    # Rendezett adatok fájlba írása
    write_file(filename, sorted_data)

    # Új elem beillesztése egy adott sorba
    sor_index = int(input("Melyik sorba szeretnéd az új számot vagy szót beilleszteni? (1-től kezdve): ")) - 1
    if sor_index < 0 or sor_index >= len(sorted_data):
        print("Hiba: Érvénytelen sorindex.")
        return

    new_elem = input("Adj meg egy új számot vagy szót: ")
    if is_number(new_elem):
        new_elem = int(new_elem)  # Ha szám, alakítsuk int-té

    # Új elem hozzáadása a megfelelő sorhoz és újrarendezés
    sorted_data[sor_index].append(new_elem)  # Új elem hozzáadása a kiválasztott sorhoz
    sorted_data[sor_index] = process_line(sorted_data[sor_index], reverse, algo_choice)  # A sor újrarendezése

    print("Frissített rendezett adatok:", sorted_data)

    # Frissített adatok visszaírása a fájlba
    write_file(filename, sorted_data)

if __name__ == "__main__":
    main()
