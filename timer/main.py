import time
from colorama import init, Fore, Style

init()

REQUIRES = ["colorama"]

def run():

    seconds = int(input("| time ?> "))

    for i in range(seconds, 0, -1):

        print(Fore.CYAN + "| " + str(i) + Style.RESET_ALL)

        time.sleep(1)

    print("| done")
