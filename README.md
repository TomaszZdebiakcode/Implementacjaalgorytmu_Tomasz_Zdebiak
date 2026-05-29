# Implementacja algorytmu A* do znajdowania najkrótszej ścieżki

## Opis projektu

Projekt implementuje algorytm A* (A-star) służący do znajdowania najkrótszej ścieżki w środowisku siatkowym (grid).

Dodatkowo zaimplementowano algorytm BFS w celu porównania wydajności obu metod.

Projekt został wykonany w ramach przedmiotu **Sztuczna Inteligencja**.

---

## Zastosowane technologie

* Python
* matplotlib
* numpy
* pytest

---

## Funkcjonalności

* implementacja algorytmu A*
* implementacja BFS
* generowanie planszy z przeszkodami
* wizualizacja znalezionej ścieżki
* pomiar czasu działania algorytmów
* porównanie liczby odwiedzonych węzłów
* eksperymenty dla różnych rozmiarów plansz

---

## Struktura projektu

```text
app/
├── astar.py
├── bfs.py
├── charts.py
├── experiments.py
├── grid.py
├── main.py
└── visualization.py

tests/
├── test_astar.py
└── test_bfs.py
```

---

## Instalacja

Instalacja wymaganych bibliotek:

```bash
pip install matplotlib numpy pytest pytest-cov
```

---

## Uruchomienie programu

```bash
python app/main.py
```

---

## Uruchomienie eksperymentów

```bash
python app/experiments.py
```

---

## Uruchomienie testów

```bash
python -m pytest
```

---

## Przykładowe wyniki

### A*

* visited nodes: 343
* path length: 39

### BFS

* visited nodes: 378
* path length: 39

Algorytm A* odwiedzał mniej węzłów niż BFS dzięki zastosowaniu heurystyki Manhattan.

---

## Autor

Tomasz Zdebiak
