import random

# Losowanie, czy pada
pada = random.choice([True, False])  # True = pada, False = nie pada
zgaduj = True

while zgaduj:
    odpowiedz = input("Czy pada? (t/n) ").lower()  # Pobieramy odpowiedź i zamieniamy na małe litery
    
    # Sprawdzamy, czy odpowiedź użytkownika jest poprawna
    if (odpowiedz == "t" and pada) or (odpowiedz == "n" and not pada):
        print("Brawo, zgadłeś!")
        zgaduj = False  # Kończymy pętlę, bo użytkownik zgadł poprawnie
    else:
        print("Spróbuj jeszcze raz.")
