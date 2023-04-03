import math

#Zad 1

def panele(dlPodlogi, szPodlogi, dlPanela, szPanela, opakowaniePaneli):
    pomieszczenie = (dlPodlogi * szPodlogi) * 1.1

    powierzchniaOpakowania = dlPanela * szPanela * opakowaniePaneli

    potrzebnePanele = math.ceil(pomieszczenie / powierzchniaOpakowania)

    potrzebneOpakowania = math.ceil(potrzebnePanele / opakowaniePaneli)
    print(f"Dlugosc podlogi: {dlPodlogi}\nSzerokosc podlogi: {szPodlogi}\nDlugosc panela: {dlPanela}"
          f"\nSzerokosc panela: {szPanela}\nIlosc paneli w opakowaniu: {opakowaniePaneli}")

    print(f"============================================================")

    print(f"Powierzchnia pomieszczenia: {pomieszczenie}\nPotrzebna ilosc opakowan: {potrzebneOpakowania}")
panele(3,3,1,0.2,5)

#zad 2

def liczbaPierwsza(*args):
    tablica = []
    for number in args:
        if number < 2:
            tablica.append(False)
        else:
            is_prime = True
            for i in range(2, int(math.sqrt(number))+1):
                if number % i == 0:
                    is_prime = False
                    break
            tablica.append(is_prime)
    return tuple(tablica)
print(liczbaPierwsza(2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))
print(f"============================================================")

#Zad 3

def szyfrCezara(tekst, klucz, alfabet='abcdefghijklmnopqrstuvwxyz'):

    wiadomosc = ''

    for char in tekst:
        if char.lower() in alfabet:
            #zostawia duza litere
            charUpper = char.isupper()
            charIndex = alfabet.index(char.lower())
            zmienionyIndex = (charIndex + klucz) % len(alfabet)
            zmienionyChar = alfabet[zmienionyIndex]
            if charUpper:
                wiadomosc += zmienionyChar.upper()
            else:
                wiadomosc += zmienionyChar
        else:
            wiadomosc += char
    return wiadomosc

tekst = "AbCdEfG123!@#"
klucz = 2
poSzyfrowaniu = szyfrCezara(tekst, klucz)
print(f"Wiadomosc przed szyfrowaniem: {tekst}\n"
      f"Wiadomosc po szyfrowaniu: {poSzyfrowaniu}")