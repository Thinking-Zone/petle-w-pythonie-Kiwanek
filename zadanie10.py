# Zadanie: Napisz program, który wypisze wszystkie liczby parzyste od 1 do 50.
# Program powinien używać pętli i sprawdzać, czy liczba jest parzysta (czyli dzieli się przez 2 bez reszty).
# Program powinien wypisać liczby parzyste w jednej linii, oddzielone spacjami.

print("A pod spodem rozwiązanie tego zadanka, napisane w Pythonie :)")

# Rozwiązanie:
for i in range(1, 51):
    if i % 2 == 0:
        print(i, end=" ")  # Wypisujemy liczbę, ale nie przechodzimy do nowej linii
