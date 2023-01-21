import os

# Czyści terminal, urzywająć komend systemowych
# odpowienio na którym systemie operacyjnym została wywołana funkcja
def clear_screen():

    # Jeżeli windows
    if os.name == 'nt':
        os.system('cls')

    else:
        os.system('clear')