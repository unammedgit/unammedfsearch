import webbrowser
import os
from colorama import init, Fore

def print_ascii_art():
    ascii_art = """
  _   _                                          _     ___     ___                           _    
 | | | |  _ _    __ _   _ __    _ __    ___   __| |   | __|   / __|  ___   __ _   _ _   __  | |_  
 | |_| | | ' \  / _` | | '  \  | '  \  / -_) / _` |   | _|    \__ \ / -_) / _` | | '_| / _| | ' \ 
  \___/  |_||_| \__,_| |_|_|_| |_|_|_| \___| \__,_|   |_|     |___/ \___| \__,_| |_|   \__| |_||_|
"""
    print(ascii_art)

def ricerca_facebook():
    init(autoreset=True)  # Inizializza colorama

    print_ascii_art()

    termine_ricercare = input("Inserisci il termine da ricercare: ")

    opzioni = [
        f"{Fore.GREEN}1{Fore.RESET} Ricerca parola nei post",
        f"{Fore.GREEN}2{Fore.RESET} Ricerca parola nei video",
        f"{Fore.GREEN}3{Fore.RESET} Ricerca parola nelle foto"
    ]

    print("\nScegli l'opzione:")
    for opzione in opzioni:
        print(opzione)

    scelta = input("\nOpzione: ")

    if scelta == "1":
        url = f"https://www.facebook.com/search/posts/?q={termine_ricercare}"
    elif scelta == "2":
        url = f"https://www.facebook.com/search/videos/?q={termine_ricercare}"
    elif scelta == "3":
        url = f"https://www.facebook.com/search/photos/?q={termine_ricercare}"
    else:
        print("Opzione non valida.")
        return

    print(f"Apertura del link: {url}")
    webbrowser.open(url)

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')  # Pulisce la console
    ricerca_facebook()