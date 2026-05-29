# Implementacja algorytmu A* do znajdowania najkrótszej ścieżki

## Opis projektu

Projekt implementuje algorytm A* (A-star) służący do znajdowania najkrótszej ścieżki w środowisku siatkowym (grid).

Dodatkowo zaimplementowano algorytm BFS w celu porównania wydajności obu metod.

Projekt został wykonany w ramach przedmiotu **Sztuczna Inteligencja**.

---

# Zastosowanie praktyczne

Projekt przedstawia system planowania trasy dla robota logistycznego obsługującego automaty vendingowe.

Robot porusza się po magazynie i musi dostarczyć napoje do wybranego automatu vendingowego. Magazyn zawiera przeszkody w postaci regałów i elementów infrastruktury.

Algorytm A* wyznacza najkrótszą trasę pomiędzy pozycją robota a docelowym automatem. Dodatkowo zaimplementowano algorytm BFS w celu porównania efektywności obu metod.

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
## Instalacja UV
python -m pip install uv

python -m uv sync

## Uruchomienie

python -m uv run python app/main.py

## Testy

python -m uv run pytest

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
