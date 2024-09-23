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
    except Exception as e:
        print(f"Hiba történt a fájl írása közben: {e}")

def check_and_convert_data(data):
    """Ellenőrzi és konvertálja az adatokat, ha számok"""
    converted_data = []
    for item in data:
        try:
            converted_data.append(int(item))  # Megpróbálja átalakítani int-té
        except ValueError:
            print(f"Hiba: '{item}' nem szám.")
            return None
    return converted_data

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

def main():
    filename = 'ki.txt'
    data = read_file(filename)

    if data is None:
        return

    # Adatok konvertálása
    data = check_and_convert_data(data)
    if data is None:
        return

    # Rendezés irányának kiválasztása
    reverse_choice = input("Válaszd ki a rendezés irányát (n: növekvő, c: csökkenő): ")
    reverse = True if reverse_choice == 'c' else False
    
    # Rendezés végrehajtása
    sorted_data = selection_sort(data, reverse)
    print("Rendezett adatok:", sorted_data)

    # Rendezett adatok fájlba írása
    write_file(filename, sorted_data)

    # Új elem beillesztése
    new_elem = input("Adj meg egy új számot: ")
    try:
        new_elem = int(new_elem)  # Próbálja átalakítani int-té
    except ValueError:
        print("Hiba: Csak számokat adhatsz meg.")
        return

    # Új elem hozzáadása és rendezés
    sorted_data.append(new_elem)  # Új elem hozzáadása
    sorted_data = selection_sort(sorted_data, reverse)  # Rendezés a beszúrás után
    print("Frissített rendezett adatok:", sorted_data)

    # Frissített adatok visszaírása a fájlba
    write_file(filename, sorted_data)

if __name__ == "__main__":
    main()
