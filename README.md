# Implementacja algorytmu A* do znajdowania najkrótszej ścieżki

## Opis projektu

Projekt implementuje algorytm A* (A-star) służący do znajdowania najkrótszej ścieżki w środowisku siatkowym (grid).

Dodatkowo projekt zawiera porównanie działania algorytmu A* z algorytmem BFS.

Projekt został wykonany w ramach przedmiotu **Sztuczna Inteligencja**.

---

## Technologie

* Python
* matplotlib
* numpy

---

## Funkcjonalności

* implementacja algorytmu A*
* implementacja BFS
* generowanie planszy z przeszkodami
* wizualizacja znalezionej ścieżki
* pomiar czasu działania algorytmów
* porównanie liczby odwiedzonych węzłów

---

## Struktura projektu

```text
app/
├── astar.py
├── bfs.py
├── grid.py
├── main.py
├── visualization.py
└── experiments.py
```

---

## Uruchomienie projektu

Instalacja bibliotek:

```bash
pip install matplotlib numpy pytest
```

Uruchomienie programu:

```bash
python app/main.py
```

---

## Testy

Uruchomienie testów:

```bash
pytest
```

---

## Przykładowe wyniki

Program wyświetla:

* długość ścieżki,
* liczbę odwiedzonych węzłów,
* czas działania algorytmów.

Dodatkowo generowana jest wizualizacja planszy.

---

## Autor

Tomasz Zdebiak

