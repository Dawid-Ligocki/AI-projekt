# Algorytm przeszukiwania tabu - Problem komiwojażera

## Opis
Ten program implementuje algorytm przeszukiwania tabu w celu rozwiązania problemu komiwojażera. Problem komiwojażera polega na znalezieniu najkrótszej trasy, która odwiedza wszystkie miasta dokładnie raz i wraca do miasta początkowego.

Algorytm przeszukiwania tabu jest metaheurystycznym algorytmem optymalizacji, który polega na iteracyjnym przeszukiwaniu przestrzeni rozwiązań, z uwzględnieniem listy tabu, która zapobiega powtarzaniu się niektórych ruchów.

## Zależności
Aby uruchomić ten program, wymagane są następujące zależności:
- Python 3.x
- Pygame

## Instrukcje
1. Zainstaluj niezbędne zależności: `pip install pygame`.
2. Uruchom program: `python main.py`.
3. Program wygeneruje losową listę miast i zastosuje algorytm przeszukiwania tabu w celu znalezienia najlepszej i najgorszej trasy.
4. Wyniki, w tym najlepsza trasa i jej długość, zostaną wyświetlone na standardowym wyjściu.
5. Po zakończeniu analizy wyników, program wyświetli animację graficzną, przedstawiającą miasta, najlepszą trasę i najgorszą trasę.

## Konfiguracja ekranu
Kod zawiera następujące zmienne konfiguracyjne dotyczące ekranu:
- WIDTH: Szerokość ekranu w pikselach.
- HEIGHT: Wysokość ekranu w pikselach.
- FPS: Liczba klatek na sekundę.
- BG_COLOR: Kolor tła ekranu.
- CITY_COLOR: Kolor miast.
- BEST_PATH_COLOR: Kolor najlepszej trasy.
- WORST_PATH_COLOR: Kolor najgorszej trasy.

## Główne funkcje
- `utworz_liste_miast(liczba_miast)`: Generuje losową listę miast na podstawie podanej liczby miast.
- `wypisz_informacje_o_miastach(miasta)`: Wypisuje informacje o współrzędnych miast na standardowe wyjście.
- `oblicz_odleglosc(miasto1, miasto2)`: Oblicza odległość między dwoma miastami na podstawie ich współrzędnych.
- `oblicz_dlugosc_trasy(trasa, miasta)`: Oblicza długość trasy dla podanej kolejności odwiedzanych miast.
- `przeszukiwanie_tabu(miasta, liczba_iteracji, rozmiar_tabu)`: Implementuje algorytm przeszukiwania tabu i zwraca najlepszą i najgorszą trasę wraz z ich długościami.

## Testowanie algorytmu
W kodzie znajduje się przykładowe testowanie algorytmu, które polega na wygenerowaniu losowej listy miast, a następnie zastosowaniu algorytmu przeszukiwania tabu w celu znalezienia najlepszej i najgorszej trasy. Wyniki są wypisywane na standardowe wyjście.

## Rysowanie wyniku
Po przeprowadzeniu testów, program uruchamia okno wizualizacji wyznaczonej trasy za pomocą biblioteki Pygame. Wyświetlane są miasta, najlepsza trasa i najgorsza trasa. Podgląd działa, dopóki użytkownik nie zamknie okna.

---
