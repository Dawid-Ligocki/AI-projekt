import random
import math
import pygame
import sys

# Konfiguracja ekranu
WIDTH = 1600
HEIGHT = 600
FPS = 60
BG_COLOR = (255, 255, 255)
CITY_COLOR = (0, 0, 0)
BEST_PATH_COLOR = (255, 0, 0)
WORST_PATH_COLOR = (0, 0, 255)


# Tworzenie losowej listy miast
def utworz_liste_miast(liczba_miast):
    miasta = []
    for i in range(liczba_miast):
        x = random.randint(50, WIDTH // 2 - 50)  # współrzędna x miasta
        y = random.randint(50, HEIGHT - 50)  # współrzędna y miasta
        miasta.append((x, y))
    return miasta


# Funkcja wypisująca informacje o miastach
def wypisz_informacje_o_miastach(miasta):
    for i, miasto in enumerate(miasta):
        print("Miasto", i + 1, ": Współrzędne:", miasto)


# Obliczanie odległości między dwoma miastami
def oblicz_odleglosc(miasto1, miasto2):
    x1, y1 = miasto1
    x2, y2 = miasto2
    odleglosc = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return odleglosc


# Obliczanie długości trasy
def oblicz_dlugosc_trasy(trasa, miasta):
    dlugosc = 0
    for i in range(len(trasa)):
        miasto1 = miasta[trasa[i]]
        miasto2 = miasta[trasa[(i + 1) % len(trasa)]]
        dlugosc += oblicz_odleglosc(miasto1, miasto2)
    return dlugosc


# Algorytm przeszukiwania tabu
def przeszukiwanie_tabu(miasta, liczba_iteracji, rozmiar_tabu):
    liczba_miast = len(miasta)
    trasa = random.sample(range(liczba_miast), liczba_miast)  # inicjalizacja losowej trasy
    najlepsza_trasa = list(trasa)
    najlepsza_dlugosc = oblicz_dlugosc_trasy(najlepsza_trasa, miasta)
    najgorsza_trasa = list(trasa)
    najgorsza_dlugosc = oblicz_dlugosc_trasy(najgorsza_trasa, miasta)
    tabu = []

    for i in range(liczba_iteracji):
        najlepsza_sasiednia_trasa = None
        najlepsza_sasiednia_dlugosc = float('inf')

        for j in range(liczba_miast - 1):
            for k in range(j + 1, liczba_miast):
                sasiednia_trasa = list(trasa)
                sasiednia_trasa[j], sasiednia_trasa[k] = sasiednia_trasa[k], sasiednia_trasa[j]

                if sasiednia_trasa not in tabu:
                    dlugosc_sasiedniej_trasy = oblicz_dlugosc_trasy(sasiednia_trasa, miasta)
                    if dlugosc_sasiedniej_trasy < najlepsza_sasiednia_dlugosc:
                        najlepsza_sasiednia_trasa = list(sasiednia_trasa)
                        najlepsza_sasiednia_dlugosc = dlugosc_sasiedniej_trasy

        trasa = list(najlepsza_sasiednia_trasa)
        dlugosc_trasy = najlepsza_sasiednia_dlugosc

        if dlugosc_trasy < najlepsza_dlugosc:
            najlepsza_trasa = list(trasa)
            najlepsza_dlugosc = dlugosc_trasy

        if dlugosc_trasy > najgorsza_dlugosc:
            najgorsza_trasa = list(trasa)
            najgorsza_dlugosc = dlugosc_trasy

        tabu.append(list(trasa))
        if len(tabu) > rozmiar_tabu:
            tabu.pop(0)

    return najlepsza_trasa, najlepsza_dlugosc, najgorsza_trasa, najgorsza_dlugosc


# Inicjalizacja Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Najlepsza(czerwony) i najgorsza(niebieski) trasa  - Algorytm przeszukiwania tabu  -  Problem komiwojażera")
clock = pygame.time.Clock()


# Funkcja rysująca miasta i trasy
def rysuj(miasta, najlepsza_trasa, najgorsza_trasa):
    screen.fill(BG_COLOR)

    # Rysowanie najlepszej trasy
    for i in range(len(najlepsza_trasa)):
        miasto1 = miasta[najlepsza_trasa[i]]
        miasto2 = miasta[najlepsza_trasa[(i + 1) % len(najlepsza_trasa)]]
        pygame.draw.line(screen, BEST_PATH_COLOR, miasto1, miasto2, 2)

    # Rysowanie najgorszej trasy
    for i in range(len(najgorsza_trasa)):
        miasto1 = miasta[najgorsza_trasa[i]]
        miasto2 = miasta[najgorsza_trasa[(i + 1) % len(najgorsza_trasa)]]
        pygame.draw.line(screen, WORST_PATH_COLOR, (miasto1[0] + WIDTH // 2, miasto1[1]),
                         (miasto2[0] + WIDTH // 2, miasto2[1]), 2)

    # Rysowanie miast na pierwszym grafie
    for miasto in miasta:
        pygame.draw.circle(screen, CITY_COLOR, miasto, 6)

    # Rysowanie miast na drugim grafie
    for miasto in miasta:
        przesuniete_miasto = (miasto[0] + WIDTH // 2, miasto[1])
        pygame.draw.circle(screen, CITY_COLOR, przesuniete_miasto, 6)

    pygame.display.flip()


# Testowanie algorytmu
liczba_miast = 10
liczba_iteracji = 10000
rozmiar_tabu = 1000

miasta = utworz_liste_miast(liczba_miast)
wypisz_informacje_o_miastach(miasta)
najlepsza_trasa, najlepsza_dlugosc, najgorsza_trasa, najgorsza_dlugosc = przeszukiwanie_tabu(miasta, liczba_iteracji,
                                                                                             rozmiar_tabu)

print("Najlepsza trasa:", najlepsza_trasa)
print("Długość trasy:", najlepsza_dlugosc)
print("Najgorsza trasa:", najgorsza_trasa)
print("Długość trasy:", najgorsza_dlugosc)

# Rozpoczęcie animacji
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    rysuj(miasta, najlepsza_trasa, najgorsza_trasa)

pygame.quit()
sys.exit()
