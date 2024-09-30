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

def insertion_sort(arr, reverse=False):
    """Beszúrásos rendezés (választható növekvő vagy csökkenő)"""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and ((key < arr[j] and not reverse) or (key > arr[j] and reverse)):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def main():
    filename = 'ki.txt'
    data = read_file(filename)

    if data is None:
        return

    # Ellenőrizzük, hogy a sorok csak számokat tartalmaznak-e, és konvertáljuk őket int-té
    try:
        data = [[int(item) for item in line] for line in data]  # Minden sor elemeit számmá alakítja
    except ValueError:
        print("Hiba: A fájl nem csak számokat tartalmaz.")
        return

    # Rendezés irányának kiválasztása
    reverse_choice = input("Válaszd ki a rendezés irányát (n: növekvő, c: csökkenő): ")
    reverse = True if reverse_choice == 'c' else False

    # Rendezési algoritmus kiválasztása
    print("Válaszd ki a rendezési algoritmust:")
    print("1. Egyszerű cserés rendezés")
    print("2. Beszúrásos rendezés")
    algo_choice = input("Add meg a választásodat (1 vagy 2): ")

    if algo_choice == '1':
        # Egyszerű cserés rendezés
        sorted_data = [selection_sort(line, reverse) for line in data]
    elif algo_choice == '2':
        # Beszúrásos rendezés
        sorted_data = [insertion_sort(line, reverse) for line in data]
    else:
        print("Érvénytelen választás. A program leáll.")
        return

    print("Rendezett adatok:", sorted_data)

    # Rendezett adatok fájlba írása
    write_file(filename, sorted_data)

    # Új elem beillesztése egy adott sorba
    sor_index = int(input("Melyik sorba szeretnéd az új számot beilleszteni? (1-től kezdve): ")) - 1
    if sor_index < 0 or sor_index >= len(sorted_data):
        print("Hiba: Érvénytelen sorindex.")
        return
    
    new_elem = input("Adj meg egy új számot: ")
    try:
        new_elem = int(new_elem)  # Próbálja átalakítani int-té
    except ValueError:
        print("Hiba: Csak számokat adhatsz meg.")
        return

    # Új elem hozzáadása a megfelelő sorhoz és újrarendezés
    sorted_data[sor_index].append(new_elem)  # Új elem hozzáadása a kiválasztott sorhoz

    if algo_choice == '1':
        sorted_data[sor_index] = selection_sort(sorted_data[sor_index], reverse)  # A sor újrarendezése
    elif algo_choice == '2':
        sorted_data[sor_index] = insertion_sort(sorted_data[sor_index], reverse)  # A sor újrarendezése
    
    print("Frissített rendezett adatok:", sorted_data)

    # Frissített adatok visszaírása a fájlba
    write_file(filename, sorted_data)

if __name__ == "__main__":
    main()
