import time
import colorama
from colorama import init, Fore
from colorama import init, Style

def run():
    seconds = int(input("| time ?> "))

    for i in range(seconds, 0, -1):
        print(Fore.cyan +"| "+ str(i) + Style.RESET_ALL)
        time.sleep(1)

    print("| done")
