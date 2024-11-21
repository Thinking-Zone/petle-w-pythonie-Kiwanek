pada = False
licznik_nie = 0

while not pada:
    odpowiedz = input("Czy pada? (tak/nie/nie wiem) ").lower()  # Pobieramy odpowiedź i zamieniamy na małe litery
    
    if odpowiedz == "tak":
        print(f"Program zakończony. Udzieliłeś {licznik_nie} odpowiedzi 'nie'.")
        pada = True  # Kończymy pętlę, bo użytkownik odpowiedział "tak"
    elif odpowiedz == "nie":
        licznik_nie += 1  # Zwiększamy licznik, jeśli odpowiedź to "nie"
    elif odpowiedz == "nie wiem":
        print("To wyjdź na zewnątrz i się dowiedz.")
    else:
        print("Proszę odpowiedz 'tak', 'nie' lub 'nie wiem'.")
