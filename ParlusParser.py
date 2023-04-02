import re

# otwórz plik z pytaniami
with open('pytania.txt', 'r', encoding='utf-8') as f:
    # odczytanie zawartości pliku i podzielenie go na linie
    lines = f.readlines()

# usunięcie pustych linii
lines = [line.strip() for line in lines if line.strip()]

# otwarcie pliku do zapisu
with open('plik.txt', 'w', encoding='utf-8') as f:
    # zapisanie linii bez pustych linii
    f.write('\n'.join(lines))
    
with open('pytania.txt', 'r', encoding='utf-8') as f:
    data = f.read()

# podziel na poszczególne pytania
pytania = re.split(r'\d+\.', data)[1:]

# dla każdego pytania zapisz w osobnym pliku
for i, p in enumerate(pytania, start=1):
    # znajdź numer pytania
    numer_pytania = f"{i:03}"
    # znajdź pytanie i odpowiedzi
    pytanie = p.split('\n')[0]
    pytanie = pytanie[1:]
    odpowiedzi = p.split('\n')[1:]
    klucz = ''
    # znajdź indeks prawidłowej odpowiedzi
    for j, o in enumerate(odpowiedzi):
        if o and o.endswith('*'):
            klucz += '1'
            indeks_prawidlowy = f"X{j:02}"
            odpowiedzi[j] = o[3:-1]
        elif o:
            klucz += '0'
            odpowiedzi[j] = o[3:]
        else:
            odpowiedzi[j] = o[3:]
    # stwórz nowy plik i zapisz pytanie i odpowiedzi
    with open(f"pytania/pytanie_{numer_pytania}.txt", 'w', encoding='utf-8') as f:
        f.write(f"X{klucz}\n{pytanie}\n")
        for o in odpowiedzi:
            f.write(f"{o}\n")
