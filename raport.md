Implementacja algorytmu A* do znajdowania najkrótszej ścieżki
Opis problemu

Celem projektu było rozwiązanie problemu znajdowania najkrótszej ścieżki pomiędzy dwoma punktami w środowisku siatkowym.

Problem ten występuje m.in. w:

grach komputerowych,
robotyce,
systemach nawigacji.
Opis danych

Środowisko zostało przedstawione jako dwuwymiarowa siatka (grid), zawierająca:

pola wolne,
przeszkody.

Plansze były generowane losowo.

Opis algorytmu

Zaimplementowano algorytm A* wykorzystujący heurystykę Manhattan.

Funkcja kosztu:

f(n) = g(n) + h(n)

gdzie:

g(n) – koszt dojścia do węzła,
h(n) – heurystyka Manhattan.

Dodatkowo zaimplementowano algorytm BFS w celu porównania wydajności.

Eksperymenty

Przeprowadzono testy dla różnych:

rozmiarów planszy,
poziomów zagęszczenia przeszkód.

Analizowano:

czas działania,
liczbę odwiedzonych węzłów,
długość ścieżki.
Wyniki

Algorytm A* znajdował najkrótszą ścieżkę szybciej niż BFS oraz odwiedzał mniejszą liczbę węzłów.

Największa różnica była widoczna dla dużych plansz.

Wnioski

Heurystyka Manhattan znacząco poprawia wydajność wyszukiwania ścieżki.

Algorytm A* jest bardziej efektywny od BFS w problemie znajdowania najkrótszej ścieżki w środowisku siatkowym.