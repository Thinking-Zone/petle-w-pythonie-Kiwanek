# Pętla "for" jest używana, gdy znamy dokładną liczbę iteracji lub gdy chcemy iterować po sekwencji (np. lista, range).
# Pętla "for" jest idealna do przetwarzania elementów z kolekcji (np. list, krotek, ciągów znaków) lub w przypadku, gdy znamy liczbę kroków.
# Pętla "while" natomiast działa, dopóki warunek jest spełniony. Używamy jej, gdy nie wiemy, ile iteracji będzie potrzebnych
# i zależymy od jakiegoś warunku logicznego (np. dopóki użytkownik nie poda poprawnej odpowiedzi).

# Przykład pętli for:
for i in range(5):
    print(i)  # Pętla wykona się dokładnie 5 razy, od 0 do 4

# Przykład pętli while:
i = 0
while i < 5:
    print(i)  # Pętla wykona się dopóki i jest mniejsze od 5
    i += 1
