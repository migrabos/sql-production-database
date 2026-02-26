#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generator danych testowych dla bazy danych produkcyjnej
Zgodny ze schematem script (7).sql
"""

from faker import Faker
import random
from datetime import datetime, timedelta, date

fake = Faker('pl_PL')
random.seed(42)  # Dla powtarzalności

# ==================== KONFIGURACJA ====================
NUM_PRACOWNICY = 15
NUM_ZAMOWIENIA = 50
NUM_KLIENCI = 20
NUM_PRODUKTY = 20
NUM_CZESCI = 40
NUM_DOSTAWCY = 5
NUM_REALIZACJI = 15
NUM_DOSTAW = 15
NUM_PRODUKCJA = 25

# Proporcje klientów
PROC_INDYWIDUALNI = 0.6  # 60% indywidualnych

# ==================== DANE SŁOWNIKOWE ====================
panstwa_dane = ['Polska', 'Niemcy', 'Czechy', 'Słowacja', 'Francja']

miejscowosci_dane = [
    ('Warszawa', 1), ('Kraków', 1), ('Gdańsk', 1), ('Wrocław', 1), ('Poznań', 1),
    ('Łódź', 1), ('Katowice', 1), ('Lublin', 1), ('Szczecin', 1), ('Bydgoszcz', 1),
    ('Berlin', 2), ('Praga', 3), ('Bratysława', 4), ('Paryż', 5), ('Lyon', 5)
]

stanowiska_dane = [
    'Dyrektor', 'Kierownik produkcji', 'Kierownik magazynu', 'Specjalista ds. sprzedaży',
    'Technik', 'Magazynier', 'Operator maszyn', 'Kontroler jakości', 'Księgowy', 'Pracownik biurowy'
]

kategorie_dane = [
    'Meble biurowe', 'Meble domowe', 'Krzesła', 'Stoły', 'Szafy',
    'Regały', 'Biurka', 'Fotele', 'Akcesoria', 'Meble ogrodowe'
]

materialy_dane = [
    ('Drewno dębowe', 'Wysokiej jakości drewno dębowe z certyfikatem FSC'),
    ('Drewno sosnowe', 'Drewno sosnowe z polskich lasów'),
    ('Stal nierdzewna', 'Stal nierdzewna klasy 304'),
    ('Aluminium', 'Profil aluminiowy anodowany'),
    ('Sklejka', 'Sklejka brzozowa 18mm'),
    ('MDF', 'Płyta MDF laminowana'),
    ('Szkło hartowane', 'Szkło hartowane 8mm'),
    ('Tworzywo sztuczne', 'Polietylen wysokiej gęstości'),
    ('Skóra naturalna', 'Skóra bydlęca garbowana'),
    ('Tkanina tapicerska', 'Tkanina poliestrowa trudnopalna'),
    ('Pianka poliuretanowa', 'Pianka HR wysokoelastyczna'),
    ('Lakier wodny', 'Lakier ekologiczny na bazie wody'),
    ('Klej montażowy', 'Klej poliuretanowy D4'),
    ('Fornir naturalny', 'Fornir dębowy 0.6mm'),
    ('Płyta wiórowa', 'Płyta wiórowa laminowana E1')
]

czesci_dane = [
    ('Noga stołu dębowa', 'Toczona noga stołu z drewna dębowego, wys. 72cm', 1),
    ('Blat stołu dębowy 140x80', 'Blat stołu z litego drewna dębowego', 1),
    ('Stelaż stalowy biurka', 'Stalowy stelaż biurka z regulacją wysokości', 3),
    ('Siedzisko krzesła', 'Siedzisko tapicerowane pianką HR', 11),
    ('Oparcie krzesła', 'Oparcie ergonomiczne z siatki', 8),
    ('Podłokietnik krzesła', 'Podłokietnik regulowany 3D', 4),
    ('Mechanizm obrotowy', 'Mechanizm obrotowy z gazowym podnośnikiem', 3),
    ('Kółka do krzesła', 'Zestaw 5 kółek poliamidowych', 8),
    ('Półka regału 80x30', 'Półka z płyty MDF laminowanej', 6),
    ('Bok szafy', 'Bok szafy z płyty wiórowej 18mm', 15),
    ('Front szuflady', 'Front szuflady z uchwytem frezowanym', 6),
    ('Prowadnica szuflady', 'Prowadnica kulkowa pełnego wysuwu', 3),
    ('Zawias meblowy', 'Zawias cichy domyk 110°', 3),
    ('Blat biurka 160x80', 'Blat biurka z płyty melaminowanej', 6),
    ('Noga biurka metalowa', 'Noga stalowa kwadratowa 60x60mm', 3),
    ('Listwa wykończeniowa', 'Listwa ABS 2mm dopasowana kolorystycznie', 8),
    ('Panel tylny szafy', 'Panel HDF 3mm lakierowany', 6),
    ('Cokół meblowy', 'Cokół regulowany PCV 100mm', 8),
    ('Uchwyt meblowy', 'Uchwyt aluminiowy profil 128mm', 4),
    ('Zamek meblowy', 'Zamek cylindryczny z kluczem', 3),
    ('Nóżka regulowana', 'Nóżka plastikowa z regulacją 0-15mm', 8),
    ('Wspornik półki', 'Wspornik niewidoczny stalowy', 3),
    ('Plecy szafy', 'Płyta HDF 3mm biała', 6),
    ('Rama fotela', 'Rama fotela z giętej sklejki', 5),
    ('Tapicerka fotela', 'Pokrycie ze skóry ekologicznej', 9),
    ('Poduszka siedziska', 'Poduszka z pianki HR 50kg/m3', 11),
    ('Oparcie fotela', 'Oparcie wyprofilowane tapicerowane', 10),
    ('Podstawa fotela', 'Podstawa 5-ramienna aluminiowa', 4),
    ('Drążek wieszakowy', 'Drążek owalny stalowy chromowany', 3),
    ('Szyna montażowa', 'Szyna do zawieszenia szafek', 3),
    ('Blat szklany', 'Blat ze szkła hartowanego 10mm', 7),
    ('Osłona kabli', 'Korytko na kable metalowe', 3),
    ('Mata antypoślizgowa', 'Mata gumowa do szuflad', 8),
    ('Odbojnik drzwi', 'Odbojnik silikonowy samoprzylepny', 8),
    ('Stopka poziomująca', 'Stopka metalowa M10', 3),
    ('Wkład szuflady', 'Organizer do szuflady drewniany', 1),
    ('Szkło do drzwi', 'Szkło satynowane 4mm', 7),
    ('Listwa LED', 'Taśma LED 12V ciepła biel', 4),
    ('Zasilacz LED', 'Zasilacz impulsowy 12V 60W', 4),
    ('Czujnik ruchu', 'Czujnik PIR do oświetlenia', 8)
]

produkty_dane = [
    ('Biurko NORDIC 160', 549.0, 'Nowoczesne biurko z drewna dębowego', 7),
    ('Krzesło ERGO PRO', 649.0, 'Ergonomiczne krzesło biurowe z siatką', 3),
    ('Szafa ALTO 200', 1299.0, 'Szafa ubraniowa z lustrem przesuwnym', 5),
    ('Regał LOFT 180', 899.0, 'Regał industrialny metal-drewno', 6),
    ('Stół FAMILY 180', 1599.0, 'Rozkładany stół jadalniany dla 8 osób', 4),
    ('Fotel COMFORT PLUS', 899.0, 'Fotel wypoczynkowy z funkcją relax', 8),
    ('Komoda SCANDI 3S', 399.0, 'Komoda z 3 szufladami w stylu skandynawskim', 2),
    ('Biurko CORNER 140', 699.0, 'Biurko narożne z półkami', 7),
    ('Krzesło MESH DELUXE', 899.0, 'Krzesło z pełnym oparciem siatkowym', 3),
    ('Stół INDUSTRIAL 160', 1299.0, 'Stół z blatem dębowym i nogami metalowymi', 4),
    ('Szafka RTV MATRIX', 599.0, 'Szafka pod telewizor z szufladami', 2),
    ('Regał BOOKS 220', 1399.0, 'Wysoki regał na książki z drabinką', 6),
    ('Fotel BOSS LEATHER', 1999.0, 'Ekskluzywny fotel skórzany obrotowy', 8),
    ('Półka CUBE 30x30', 299.0, 'Modułowa półka ścienna', 6),
    ('Biurko SIMPLE 120', 399.0, 'Proste biurko z szufladą', 7),
    ('Krzesło KIDS COLOR', 199.0, 'Krzesło dziecięce z regulacją', 3),
    ('Szafa SLIDE 250', 2499.0, 'Szafa z drzwiami przesuwnymi 250cm', 5),
    ('Stół CAFE okrągły', 249.0, 'Stolik kawowy okrągły 80cm', 4),
    ('Wieszak TREE', 299.0, 'Wieszak stojący w kształcie drzewa', 9),
    ('Ławka GARDEN 150', 399.0, 'Ławka ogrodowa drewniana', 10)
]

metody_platnosci_dane = ['Gotówka', 'Karta płatnicza', 'Przelew bankowy', 'BLIK', 'Raty 0%', 'PayPal']

stany_zamowienia_dane = [
    'Nowe', 'W realizacji', 'Skompletowane', 'Wysłane', 'Dostarczone', 'Zakończone'
]

dostawcy_dane = [
    ('Drewno-Pol Sp. z o.o.', 'kontakt@drewnopol.pl', '+48123456789'),
    ('Metal-System S.A.', 'biuro@metalsystem.pl', '+48234567890'),
    ('Tapicernia Kowalski', 'zamowienia@tapkowal.pl', '+48345678901'),
    ('Glass&More', 'info@glassmore.pl', '+48456789012'),
    ('Okucia Premium', 'sprzedaz@okucprem.pl', '+48567890123')
]

# ==================== GENEROWANIE DANYCH ====================

# 1. PAŃSTWA
panstwa = [{'PaństwoID': i+1, 'Nazwa': n} for i, n in enumerate(panstwa_dane)]

# 2. MIEJSCOWOŚCI
miejscowosci = [{'MiejscowośćID': i+1, 'Nazwa': m[0], 'PaństwoID': m[1]} for i, m in enumerate(miejscowosci_dane)]

# 3. STANOWISKA
stanowiska = [{'StanowiskoID': i+1, 'Nazwa': n} for i, n in enumerate(stanowiska_dane)]

# 4. KATEGORIE
kategorie = [{'KategoriaID': i+1, 'Nazwa': n} for i, n in enumerate(kategorie_dane)]

# 5. MATERIAŁY
materialy = [{'MateriałID': i+1, 'Nazwa': m[0], 'Opis': m[1]} for i, m in enumerate(materialy_dane)]

# 6. METODY_PŁATNOŚCI
metody_platnosci = [{'MetodaID': i+1, 'Opis': m} for i, m in enumerate(metody_platnosci_dane)]

# 7. STANY
stany = [{'StanID': i+1, 'Opis': s} for i, s in enumerate(stany_zamowienia_dane)]

# 8. DOSTAWCY
dostawcy = [{'DostawcaID': i+1, 'NazwaDostawcy': d[0], 'Email': d[1], 'NumerTelefonu': d[2]} for i, d in enumerate(dostawcy_dane)]

# 9. CZĘŚCI  
czesci = [{'CzęśćID': i+1, 'Nazwa': c[0], 'Opis': c[1], 'MateriałID': c[2]} for i, c in enumerate(czesci_dane)]

# 10. PRODUKTY
produkty = []
for i, p in enumerate(produkty_dane):
    produkty.append({
        'ProduktID': i+1,
        'Nazwa': p[0],
        'CenaJednostkowa': p[1],
        'Opis': p[2],
        'KategoriaID': p[3],
        'CzyDostępny': random.random() > 0.1  # 90% dostępnych
    })

# 11. KLIENCI (z unikalnymi emailami i telefonami)
klienci = []
klienci_indywidualni = []
firmy = []
used_emails = set()
used_phones = set()

num_indywidualni = int(NUM_KLIENCI * PROC_INDYWIDUALNI)
num_firmy = NUM_KLIENCI - num_indywidualni

for i in range(NUM_KLIENCI):
    kid = i + 1
    
    # Generuj unikalny email
    while True:
        if i < num_indywidualni:
            email = f"klient{kid}@{fake.free_email_domain()}"
        else:
            email = f"firma{kid}@{fake.free_email_domain()}"
        if email not in used_emails and len(email) <= 30:
            used_emails.add(email)
            break
    
    # Generuj unikalny telefon
    while True:
        phone = f"+48{random.randint(100000000, 999999999)}"
        if phone not in used_phones:
            used_phones.add(phone)
            break
    
    klient = {
        'KlientID': kid,
        'Email': email,
        'NumerTelefonu': phone,
        'MiejscowośćID': random.randint(1, len(miejscowosci)),
        'KodPocztowy': f"{random.randint(10,99)}-{random.randint(100,999)}",
        'Ulica': fake.street_name()[:50] if random.random() > 0.2 else None,
        'NrBudynku': str(random.randint(1, 200)),
        'NrLokalu': str(random.randint(1, 50)) if random.random() > 0.4 else None
    }
    klienci.append(klient)
    
    if i < num_indywidualni:
        klienci_indywidualni.append({
            'KlientID': kid,
            'Imię': fake.first_name()[:50],
            'Nazwisko': fake.last_name()[:50]
        })
    else:
        firmy.append({
            'KlientID': kid,
            'Nazwa': fake.company()[:50]
        })

# 12. PRACOWNICY (z unikalnymi emailami i telefonami)
pracownicy = []
used_emp_emails = set()
used_emp_phones = set()

for i in range(NUM_PRACOWNICY):
    pid = i + 1
    
    # Generuj unikalny email
    while True:
        first = fake.first_name()[:15]
        last = fake.last_name()[:15]
        email = f"{first.lower()}.{last.lower()[:8]}@firma.pl"
        if email not in used_emp_emails and len(email) <= 30:
            used_emp_emails.add(email)
            break
    
    # Generuj unikalny telefon
    while True:
        phone = f"+48{random.randint(100000000, 999999999)}"
        if phone not in used_emp_phones and phone not in used_phones:
            used_emp_phones.add(phone)
            break
    
    # Data urodzenia i zatrudnienia
    data_ur = date(random.randint(1970, 1995), random.randint(1, 12), random.randint(1, 28))
    data_zatr = date(random.randint(2015, 2024), random.randint(1, 12), random.randint(1, 28))
    
    # Przełożony - pierwszy pracownik jest szefem (bez przełożonego)
    przelozony = None if pid <= 2 else random.randint(1, min(pid-1, 3))
    
    pracownicy.append({
        'PracownikID': pid,
        'Imię': first[:30],
        'Nazwisko': last[:30],
        'Email': email,
        'NumerTelefonu': phone,
        'DataUrodzenia': data_ur,
        'DataZatrudnienia': data_zatr,
        'StanowiskoID': min(pid, len(stanowiska)) if pid <= 3 else random.randint(4, len(stanowiska)),
        'PrzełożonyID': przelozony,
        'MiejscowośćID': random.randint(1, min(10, len(miejscowosci))),
        'KodPocztowy': f"{random.randint(10,99)}-{random.randint(100,999)}",
        'Ulica': fake.street_name()[:50] if random.random() > 0.3 else None,
        'NrBudynku': str(random.randint(1, 150)),
        'NrLokalu': str(random.randint(1, 30)) if random.random() > 0.5 else None
    })

# 13. PŁATNOŚCI i 14. ZAMÓWIENIA (generowane razem)
platnosci = []
zamowienia = []

for i in range(NUM_ZAMOWIENIA):
    zam_id = i + 1
    plat_id = i + 1
    
    # Starsze zamówienia
    days_ago = random.randint(30, 700)
    data_zam = datetime.now() - timedelta(days=days_ago)
    
    # Stan zamówienia - starsze zwykle zakończone
    if days_ago > 60:
        stan_id = 6  # Zakończone
        data_wyk = data_zam + timedelta(days=random.randint(3, 14))
    elif days_ago > 30:
        stan_id = random.choice([4, 5, 6])
        data_wyk = data_zam + timedelta(days=random.randint(3, 14)) if stan_id >= 5 else None
    else:
        stan_id = random.randint(1, 4)
        data_wyk = None
    
    # Płatność po zamówieniu
    data_plat = data_zam + timedelta(hours=random.randint(1, 48))
    
    platnosci.append({
        'PłatnośćID': plat_id,
        'MetodaID': random.randint(1, len(metody_platnosci)),
        'DataPłatności': data_plat
    })
    
    # Termin preferowany - musi być w przyszłości (GETDATE() w constraint)
    termin = datetime.now() + timedelta(days=random.randint(7, 60))
    
    zamowienia.append({
        'ZamówienieID': zam_id,
        'DataZamówienia': data_zam,
        'DataWykonania': data_wyk,
        'PracownikID': random.randint(1, NUM_PRACOWNICY),
        'KlientID': random.randint(1, NUM_KLIENCI),
        'PłatnośćID': plat_id,
        'TerminPreferowany': termin,
        'StanZamówieniaID': stan_id
    })

# 15. SZCZEGÓŁY_ZAMÓWIENIA
szczegoly_zamowienia = []
for zam in zamowienia:
    num_prods = random.randint(1, 3)
    prods = random.sample(range(1, NUM_PRODUKTY + 1), num_prods)
    for pid in prods:
        prod = produkty[pid - 1]
        szczegoly_zamowienia.append({
            'ZamówienieID': zam['ZamówienieID'],
            'ProduktID': pid,
            'IlośćProduktu': random.randint(1, 10),
            'CenaJednostkowa': prod['CenaJednostkowa'],
            'Rabat': round(random.choice([0, 0, 0, 0.05, 0.1, 0.15, 0.2]), 2)
        })

# 16. STAN_ZAMÓWIENIA (historia stanów)
stan_zamowienia = []
for zam in zamowienia:
    data_start = zam['DataZamówienia']
    akt_stan = zam['StanZamówieniaID']
    current_date = data_start
    
    for sid in range(1, akt_stan + 1):
        is_last = (sid == akt_stan)
        od = current_date
        
        if is_last:
            do = None  # Aktualny stan
        else:
            # Poprzednie stany - DoKiedy musi być > OdKiedy
            do = od + timedelta(days=random.randint(1, 3), hours=random.randint(2, 20))
        
        stan_zamowienia.append({
            'ZamówienieID': zam['ZamówienieID'],
            'StanID': sid,
            'OdKiedy': od,
            'DoKiedy': do
        })
        
        if do:
            current_date = do

# 17. STRUKTURA_PRODUKTU (jakie części składają się na produkt)
struktura_produktu = []
for prod in produkty:
    num_parts = random.randint(3, 8)
    parts = random.sample(range(1, len(czesci) + 1), min(num_parts, len(czesci)))
    for cid in parts:
        struktura_produktu.append({
            'ProduktID': prod['ProduktID'],
            'CzęśćID': cid,
            'Ilość': random.randint(1, 6)
        })

# 18. SZCZEGÓŁY_PRODUKTU (wersje produktów z historią)
szczegoly_produktu = []
sp_id = 1
for prod in produkty:
    num_versions = random.randint(1, 3)
    base_date = datetime.now() - timedelta(days=365 * 3)  # 3 lata wstecz
    
    for v in range(num_versions):
        wazny_od = base_date + timedelta(days=v * 365)
        
        if v < num_versions - 1:
            # Poprzednie wersje - mają WażnyDo
            wazny_do = wazny_od + timedelta(days=random.randint(180, 364))
        else:
            # Aktualna wersja - WażnyDo = NULL
            wazny_do = None
        
        koszt = round(prod['CenaJednostkowa'] * random.uniform(0.3, 0.5), 2)
        robocizna = round(prod['CenaJednostkowa'] * random.uniform(0.1, 0.2), 2)
        
        szczegoly_produktu.append({
            'ProduktSzczegółyID': sp_id,
            'KosztProdukcji': koszt,
            'CzasProdukcji': round(random.uniform(1, 40), 2),
            'WażnyOd': wazny_od,
            'WażnyDo': wazny_do,
            'ProduktID': prod['ProduktID'],
            'Robocizna': robocizna
        })
        sp_id += 1

# 19. MAGAZYN_PRODUKTÓW
magazyn_produktow = []
for prod in produkty:
    min_il = random.randint(5, 50)
    maks_il = min_il + random.randint(50, 200)
    magazyn_produktow.append({
        'ProduktID': prod['ProduktID'],
        'Stan': random.randint(min_il, maks_il),
        'MinimalnaIlość': min_il,
        'MaksymalnaIlość': maks_il,
        'OstatniaAktualizacja': datetime.now() - timedelta(days=random.randint(0, 30))
    })

# 20. MAGAZYN_CZĘŚCI
magazyn_czesci = []
for cz in czesci:
    min_il = random.randint(20, 200)
    maks_il = min_il + random.randint(100, 800)
    magazyn_czesci.append({
        'CzęśćID': cz['CzęśćID'],
        'Stan': random.randint(min_il // 2, maks_il),
        'MinimalnaIlość': min_il,
        'MaksymalnaIlość': maks_il,
        'OstatniaAktualizacja': datetime.now() - timedelta(days=random.randint(0, 30))
    })

# 21. REALIZACJA_DOSTAWY
realizacja_dostawy = []
for i in range(NUM_REALIZACJI):
    realizacja_dostawy.append({
        'RealizacjaID': i + 1,
        'DostawcaID': random.randint(1, NUM_DOSTAWCY),
        'CzęśćID': random.randint(1, len(czesci)),
        'KosztCzęści': round(random.uniform(10, 150), 2),
        'CzasRealizacji': round(random.uniform(1, 10), 2)
    })

# 22. DOSTAWY_CZĘŚCI
dostawy_czesci = []
for i in range(NUM_DOSTAW):
    data_zam = datetime.now() - timedelta(days=random.randint(30, 300))
    data_dor = data_zam + timedelta(days=random.randint(3, 14)) if random.random() > 0.15 else None
    
    realiz = realizacja_dostawy[i % len(realizacja_dostawy)]
    dostawy_czesci.append({
        'DostawaID': i + 1,
        'DataZamówienia': data_zam,
        'DataDoręczenia': data_dor,
        'Ilość': random.randint(50, 500),
        'KosztCzęści': realiz['KosztCzęści'],
        'RealizacjaID': realiz['RealizacjaID']
    })

# 23. PRODUKCJA
produkcja = []
for i in range(NUM_PRODUKCJA):
    data_wpisu = datetime.now() - timedelta(days=random.randint(7, 500))
    # DataRozpoczęcia >= DataWpisu
    data_rozp = data_wpisu + timedelta(hours=random.randint(1, 24))
    # DataZakończenia >= DataRozpoczęcia (lub NULL)
    if (datetime.now() - data_wpisu).days > 7:
        # Starsze - zakończone
        data_zak = data_rozp + timedelta(hours=random.randint(4, 48))
    else:
        # Nowsze - mogą być w trakcie
        data_zak = data_rozp + timedelta(hours=random.randint(4, 48)) if random.random() > 0.3 else None
    
    produkcja.append({
        'ProdukcjaID': i + 1,
        'ProduktID': random.randint(1, NUM_PRODUKTY),
        'PracownikID': random.randint(1, NUM_PRACOWNICY),
        'Ilość': random.randint(1, 20),
        'DataWpisu': data_wpisu,
        'DataRozpoczęcia': data_rozp,
        'DataZakończenia': data_zak
    })

# ==================== GENEROWANIE SQL ====================

def escape_sql(val):
    """Konwertuje wartość Python na format SQL"""
    if val is None:
        return 'NULL'
    elif isinstance(val, bool):
        return '1' if val else '0'
    elif isinstance(val, (int, float)):
        return str(val)
    elif isinstance(val, datetime):
        return f"'{val.strftime('%Y-%m-%d %H:%M:%S')}'"
    elif isinstance(val, date):
        return f"'{val.strftime('%Y-%m-%d')}'"
    else:
        # Escape pojedynczy apostrof
        return f"'{str(val).replace(chr(39), chr(39)+chr(39))}'"


# Lista tabel z kolumnami IDENTITY - zgodna z script (7).sql
IDENTITY_TABLES = {
    'Państwa',              # PaństwoID IDENTITY(1,1)
    'Miejscowości',         # MiejscowośćID IDENTITY(1,1)
    'Stanowiska',           # StanowiskoID IDENTITY(1,1)
    'Kategorie',            # KategoriaID IDENTITY(1,1)
    'Materiały',            # MateriałID IDENTITY(1,1)
    'Części',               # CzęśćID IDENTITY(1,1)
    'Produkty',             # ProduktID IDENTITY(1,1)
    'Dostawcy',             # DostawcaID IDENTITY(1,1)
    'Klienci',              # KlientID IDENTITY(1,1)
    'Pracownicy',           # PracownikID IDENTITY(1,1)
    'Płatności',            # PłatnośćID IDENTITY(1,1)
    'Zamówienia',           # ZamówienieID IDENTITY(1,1)
    'Szczegóły_produktu',   # ProduktSzczegółyID IDENTITY(1,1)
    'Produkcja',            # ProdukcjaID IDENTITY(1,1)
    'Metody_płatności',     # MetodaID IDENTITY(1,1)
    'Stany',                # StanID IDENTITY(1,1)
    'Dostawy_Części',       # DostawaID IDENTITY(1,1)
    'Realizacja_Dostawy'    # RealizacjaID IDENTITY(1,1)
}
# Tabele BEZ IDENTITY: Stan_zamówienia, Szczegóły_zamówienia, Struktura_produktu,
#                      Magazyn_produktów, Magazyn_części, Firmy, Klienci_indywidualni


def generate_inserts(table_name, data, columns):
    """Generuje INSERT dla danej tabeli"""
    if not data:
        return ""
    
    has_identity = table_name in IDENTITY_TABLES
    sql = f"\n-- {table_name}\n"
    
    if has_identity:
        sql += f"SET IDENTITY_INSERT [dbo].[{table_name}] ON;\n"
    
    for row in data:
        values = ', '.join([escape_sql(row.get(col)) for col in columns])
        cols = ', '.join([f'[{col}]' for col in columns])
        sql += f"INSERT INTO [dbo].[{table_name}] ({cols}) VALUES ({values});\n"
    
    if has_identity:
        sql += f"SET IDENTITY_INSERT [dbo].[{table_name}] OFF;\n"
    
    return sql


# ==================== ZAPIS DO PLIKU ====================
with open('insert_data.sql', 'w', encoding='utf-8') as f:
    f.write("USE [u_grabos]\nGO\n\n")
    
    # Tabele słownikowe (bazowe)
    f.write(generate_inserts('Państwa', panstwa, ['PaństwoID', 'Nazwa']))
    f.write(generate_inserts('Miejscowości', miejscowosci, ['MiejscowośćID', 'Nazwa', 'PaństwoID']))
    f.write(generate_inserts('Stanowiska', stanowiska, ['StanowiskoID', 'Nazwa']))
    f.write(generate_inserts('Kategorie', kategorie, ['KategoriaID', 'Nazwa']))
    f.write(generate_inserts('Materiały', materialy, ['MateriałID', 'Nazwa', 'Opis']))
    f.write(generate_inserts('Metody_płatności', metody_platnosci, ['MetodaID', 'Opis']))
    f.write(generate_inserts('Stany', stany, ['StanID', 'Opis']))
    f.write(generate_inserts('Dostawcy', dostawcy, ['DostawcaID', 'NazwaDostawcy', 'Email', 'NumerTelefonu']))
    
    # Tabele główne
    f.write(generate_inserts('Części', czesci, ['CzęśćID', 'Nazwa', 'Opis', 'MateriałID']))
    f.write(generate_inserts('Produkty', produkty, ['ProduktID', 'Nazwa', 'CenaJednostkowa', 'Opis', 'KategoriaID', 'CzyDostępny']))
    
    # Klienci z podtypami
    f.write(generate_inserts('Klienci', klienci, ['KlientID', 'Email', 'NumerTelefonu', 'MiejscowośćID', 'KodPocztowy', 'Ulica', 'NrBudynku', 'NrLokalu']))
    f.write(generate_inserts('Klienci_indywidualni', klienci_indywidualni, ['KlientID', 'Imię', 'Nazwisko']))
    f.write(generate_inserts('Firmy', firmy, ['KlientID', 'Nazwa']))
    
    # Pracownicy
    f.write(generate_inserts('Pracownicy', pracownicy, ['PracownikID', 'Imię', 'Nazwisko', 'Email', 'NumerTelefonu', 'DataUrodzenia', 'DataZatrudnienia', 'StanowiskoID', 'PrzełożonyID', 'MiejscowośćID', 'KodPocztowy', 'Ulica', 'NrBudynku', 'NrLokalu']))
    
    # Zamówienia (Płatności muszą być przed Zamówieniami!)
    f.write(generate_inserts('Płatności', platnosci, ['PłatnośćID', 'MetodaID', 'DataPłatności']))
    f.write(generate_inserts('Zamówienia', zamowienia, ['ZamówienieID', 'DataZamówienia', 'DataWykonania', 'PracownikID', 'KlientID', 'PłatnośćID', 'TerminPreferowany', 'StanZamówieniaID']))
    f.write(generate_inserts('Szczegóły_zamówienia', szczegoly_zamowienia, ['ZamówienieID', 'ProduktID', 'IlośćProduktu', 'CenaJednostkowa', 'Rabat']))
    f.write(generate_inserts('Stan_zamówienia', stan_zamowienia, ['ZamówienieID', 'StanID', 'OdKiedy', 'DoKiedy']))
    
    # Produkty - szczegóły i struktura
    f.write(generate_inserts('Struktura_produktu', struktura_produktu, ['ProduktID', 'CzęśćID', 'Ilość']))
    f.write(generate_inserts('Szczegóły_produktu', szczegoly_produktu, ['ProduktSzczegółyID', 'KosztProdukcji', 'CzasProdukcji', 'WażnyOd', 'WażnyDo', 'ProduktID', 'Robocizna']))
    
    # Magazyny
    f.write(generate_inserts('Magazyn_produktów', magazyn_produktow, ['ProduktID', 'Stan', 'MinimalnaIlość', 'MaksymalnaIlość', 'OstatniaAktualizacja']))
    f.write(generate_inserts('Magazyn_części', magazyn_czesci, ['CzęśćID', 'Stan', 'MinimalnaIlość', 'MaksymalnaIlość', 'OstatniaAktualizacja']))
    
    # Dostawy (Realizacja_Dostawy przed Dostawy_Części!)
    f.write(generate_inserts('Realizacja_Dostawy', realizacja_dostawy, ['RealizacjaID', 'DostawcaID', 'CzęśćID', 'KosztCzęści', 'CzasRealizacji']))
    f.write(generate_inserts('Dostawy_Części', dostawy_czesci, ['DostawaID', 'DataZamówienia', 'DataDoręczenia', 'Ilość', 'KosztCzęści', 'RealizacjaID']))
    
    # Produkcja
    f.write(generate_inserts('Produkcja', produkcja, ['ProdukcjaID', 'ProduktID', 'PracownikID', 'Ilość', 'DataWpisu', 'DataRozpoczęcia', 'DataZakończenia']))

print("Wygenerowano plik insert_data.sql!")
print(f"""
Statystyki:
- Państwa: {len(panstwa)}
- Miejscowości: {len(miejscowosci)}
- Stanowiska: {len(stanowiska)}
- Pracownicy: {len(pracownicy)}
- Kategorie: {len(kategorie)}
- Materiały: {len(materialy)}
- Części: {len(czesci)}
- Produkty: {len(produkty)}
- Dostawcy: {len(dostawcy)}
- Klienci: {len(klienci)} (indywidualni: {len(klienci_indywidualni)}, firmy: {len(firmy)})
- Zamówienia: {len(zamowienia)}
- Szczegóły zamówień: {len(szczegoly_zamowienia)}
- Stan zamówienia (historia): {len(stan_zamowienia)}
- Struktura produktu: {len(struktura_produktu)}
- Szczegóły produktu: {len(szczegoly_produktu)}
- Magazyn produktów: {len(magazyn_produktow)}
- Magazyn części: {len(magazyn_czesci)}
- Realizacja dostaw: {len(realizacja_dostawy)}
- Dostawy części: {len(dostawy_czesci)}
- Produkcja: {len(produkcja)}
""")
