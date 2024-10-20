filename = 'ki.txt'


def is_number(szam):  #fuggveny arra hogy leellenorizze hogy szam e vagy sem
    try:              #a try elosegiti hogy ne dobjon ki hibauzenetet ha nem szamot kapunk
        float(szam)   #a float paranccsal megnezi hogy az adott sor/karakter lebegopontos(tizedestortte) szamma alakithato e ha igen akkor az alapertek true lesz ha pedig nem akkor false marad.
        return True   #azert float-ot hasznalunk mert ezzel a legegyszerubb megallapittani mert barmilyen szamot kepes felismerni
    except ValueError:#ezzel fogjuk meg azt a hibauzenetet amit kiirna a program es ekkor atallitjuk az erteket false-ra
        return False


def rendez(line, csokkeno, algoritmus): #rendezesi algoritmusok ugye ket opcio van az egyes az egyszeru cseres rendezes a kettes pedig a beszurasos rendezes
    if all(is_number(item) for item in line):  #ha minden item szam akkor a lambda(ez egy egyszeru fuggveny es igy nincs szukseg meg tobb def-re) x marad es nem valtozik semmi
        line = [int(item) for item in line]  
        key = lambda x: x
    else: #ha pedig betu akkor a lambda egyenlo lesz a szavak hosszusagaval ezert kell megadni a len-t az x-nek
        key = lambda x: len(x)  

    if algoritmus == '1':  
        n = len(line) 
        for i in range(n):
            minimum = i #o a kezdo elemunk ehhez kezdjuk el hasonlitani a tobbit
            for j in range(i + 1, n):
                if (key(line[j]) < key(line[minimum]) and not csokkeno) or (key(line[j]) > key(line[minimum]) and csokkeno):#elkezd vegigmenni a soron es ha talal annal kisebb szamot vagy rovidebb szoveget akkor a minimum a j elem lesz, ha nem novekvo sorrendbe rakjuk akkor ott az or amiben pedig ugynaze megy vegbe csak nem kisebbet keres hanem nagyobbat nala
                    minimum = j
            line[i], line[minimum] = line[minimum], line[i] #ezutan megvaltoztatja a sorrendet es felcsereli az i-edik elemet a minimummal, majd ezt addig folytatja mig a minimum elem vegig tud menni ugy a soron hogy nem talal nala kiseeb szamot vagy rovidebb szoveget, ha nem novekvo sorrendbe rakjuk akkor pedig ugyanez csak a nagyobbal csereli
    elif algoritmus == '2':  
        for i in range(1, len(line)):
            key_value = line[i] #mindig az i-edik elem a kulcsitem amelyet bele akarunk szoritan a rendezett helyekbe
            j = i - 1 #a j-edik elem mindig egyel kevesebb mint az i-edik elem ugyanis mindig az elotte levovel hasonlitjuk ossze 
            while j >= 0 and ((key(key_value) < key(line[j]) and not csokkeno) or (key(key_value) > key(line[j]) and csokkeno)): #hogyha a kulcsertek kisebb a j-edik elemnel akkor beilleszti a megfelelo helyre vagy az or-nal pedig nagyobb a j-edik elemnel ezt addig csinalja mig oda nem er hogy nem talal nala kisebb vagy nagyobb szamot 
                line[j + 1] = line[j]
                j -= 1
            line[j + 1] = key_value #a j+1-edik elem lesz a kulcsertek vagyis az uj i-edik elem
    else:
        print("Hiba: Érvénytelen rendezési algoritmus.")
    return line

def menu(): #foprogram futtatasa
    try: #ugyanaz a feladarta mint legutobb
        with open(filename, 'r') as file:  #fajl megnyitasa es olvasasa
            lines = file.read().strip().splitlines() #sorokra bontas
        data = [line.split(';') for line in lines] #spliteles
    except FileNotFoundError: #ennek is
        print(f"Hiba: {filename} nem található.")
        data = None

    if data is None: #kidob a gecibexd
        quit()


    rendezi = input("Válaszd ki a rendezés irányát (n: növekvő, c: csökkenő): ")
    csokkeno = True if rendezi == 'c' else False #csokken=true novekvo=false


    print("Válaszd ki a rendezési algoritmust:")
    print("1. Egyszerű cserés rendezés")
    print("2. Beszúrásos rendezés")
    algoritmus = input("Add meg a választásodat (1 vagy 2): ") #itt adjuk meg hogy az algoritmus fuggvenyben melyiket hasznaljuk
    rendezett = [rendez(line, csokkeno, algoritmus) for line in data] #itt meghivjuk a fuggvenyt amivel rendezzuk a fajl tartalmait
    print("Rendezett adatok:", rendezett)


    try:#ugynaz
        with open(filename, 'w') as file: #megnyitjuk irasra a fajlt
            for line in rendezett:
                file.write(';'.join(map(str, line)) + '\n') #visszairja az adatokat rendezve egy enterrel a vegen pontos vesszovel
    except Exception as e:#ugyanaz
        print(f"Hiba történt a fájl írása közben: {e}")

    ok = True
    while ok: #while ciklus hogy mindig tudjuk uj itemet beilleszteni
        sor_index = int(input("Melyik sorba szeretnéd az új számot vagy szót beilleszteni? (1-től kezdve, vagy írj 'kilépés'-t a befejezéshez): ")) - 1 #int-kent kerjuk be ugyanis az idexet kerjuk es azert vonunk ki belole egyet hogy igy ne kelljen nullaval kezdenunk hanem az elso elem lesz a nulladik sor de a kivonas miatt mi irhatunk egyest
        if sor_index < 0 or sor_index >= len(rendezett): #ellenorzi hogy az index szam helyes e
            print("Hiba: Érvénytelen sorindex.")
            continue #ezutan folytassa a programot ha nem jo akkor kerjunk egy ujat

        new_elem = input("Adj meg egy új számot vagy szót: ") 
        if is_number(new_elem): #ellenorzi hogy szam vagy betu
            new_elem = int(new_elem)

        rendezett[sor_index].append(new_elem) #appendel eloszor az itemet
        rendezett[sor_index] = rendez(rendezett[sor_index], csokkeno, algoritmus)#itt pedig a hasznalt fuggvennyel kiirjuk rendezve a sorokat ujra

        print("Frissített rendezett adatok:", rendezett)


        try:
            with open(filename, 'w') as file: #ugyanazok
                for line in rendezett:
                    file.write(';'.join(map(str, line)) + '\n') #visszairja helyesen a dolgokat az uj adatokkat
        except Exception as e:
            print(f"Hiba történt a fájl írása közben: {e}")

menu()