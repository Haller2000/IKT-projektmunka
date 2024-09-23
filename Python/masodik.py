def read_file(filename):
    """Fájl beolvasása és adatok listába mentése"""
    try:
        with open(filename, 'r') as file:
            data = file.read().splitlines()  # Soronként olvas, eltávolítja a sortörést
        return data
    except FileNotFoundError:
        print(f"Hiba: {filename} nem található.")
        return None

def write_file(filename, data):
    """Rendezett adatok visszaírása a fájlba"""
    try:
        with open(filename, 'w') as file:
            for item in data:
                file.write(f"{item}\n")  # Soronként írja vissza az adatokat
        print(f"A {filename} fájl frissítve lett.")
    except Exception as e:
        print(f"Hiba történt a fájl írása közben: {e}")

def check_and_convert_data(data):
    """
    Eldönti, hogy a lista számokat vagy szövegeket tartalmaz.
    Ha számokat tartalmaz, azokat int-té alakítja.
    Ha vegyes vagy hibás adatot tartalmaz, visszatér hibaüzenettel.
    """
    is_numeric = True
    for item in data:
        if not item.isdigit():  # Ellenőrzi, hogy az elem szám-e
            is_numeric = False
            break

    if is_numeric:
        return [int(item) for item in data]  # Számok int-té konvertálása
    else:
        return data  # Szöveges adatok hagyása

# Egyszerű cserés rendezés
def selection_sort(arr, reverse=False):
    """Egyszerű cserés rendezés (választható növekvő vagy csökkenő)"""
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if (arr[j] < arr[min_index] and not reverse) or (arr[j] > arr[min_index] and reverse):
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# Quicksort (második algoritmus)
def quicksort(arr, reverse=False):
    """Quicksort algoritmus (választható növekvő vagy csökkenő)"""
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if (x < pivot and not reverse) or (x > pivot and reverse)]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if (x > pivot and not reverse) or (x < pivot and reverse)]
    return quicksort(left, reverse) + middle + quicksort(right, reverse)

# Új elem beszúrása
def insert_element(arr, elem, reverse=False):
    """Új elem beszúrása a megfelelő helyre kereséssel"""
    arr.append(elem)
    arr = quicksort(arr, reverse)  # Rendezés a beszúrás után
    return arr

def main():
    # Fájl beolvasása
    filename = 'ki.txt'
    data = read_file(filename)
    
    if data is None:
        return

    # Adatok típusának eldöntése és konvertálás, ha számok
    data = check_and_convert_data(data)
    
    # Rendezési típus választása
    sort_choice = input("Válaszd ki a rendezési algoritmust (1: egyszerű cserés rendezés, 2: Quicksort): ")
    reverse_choice = input("Válaszd ki a rendezés irányát (n: növekvő, c: csökkenő): ")
    reverse = True if reverse_choice == 'c' else False
    
    # Rendezés végrehajtása
    if sort_choice == '1':
        sorted_data = selection_sort(data, reverse)
        print("Rendezett adatok (Egyszerű cserés rendezés):", sorted_data)
    elif sort_choice == '2':
        sorted_data = quicksort(data, reverse)
        print("Rendezett adatok (Quicksort):", sorted_data)
    else:
        print("Helytelen választás.")
        return

    # Rendezett adatok fájlba írása
    write_file(filename, sorted_data)

    # Új elem beszúrása
    new_elem = input("Adj meg egy új elemet: ")
    
    # Új elem típusának eldöntése
    if isinstance(data[0], int):  # Ha számok vannak
        try:
            new_elem = int(new_elem)
        except ValueError:
            print("Hiba: Csak számokat adhatsz meg.")
            return
    # A szöveges adatokat nem szükséges konvertálni

    updated_data = insert_element(sorted_data, new_elem, reverse)
    print("Az új elem beillesztése után rendezett adatok:", updated_data)

    # Frissített adatok visszaírása a fájlba
    write_file(filename, updated_data)

if __name__ == "__main__":
    main()
