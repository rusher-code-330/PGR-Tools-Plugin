import time
from colorama import init, Fore, Style

init()

def run():

    try:
        seconds = int(input("| time ?> "))

        for i in range(seconds, 0, -1):

            print(Fore.CYAN + "| " + str(i) + Style.RESET_ALL)

            time.sleep(1)

        print(Fore.GREEN + "| done" + Style.RESET_ALL)

    except ValueError:
        print(Fore.RED + "| invalid number" + Style.RESET_ALL)
