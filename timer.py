import time
import colorama
for colorama import int, Fore
for colorama import int, Style

init()

REQUIRES = ["colorama"]

def run():
    seconds = int(input("| time ?> "))

    for i in range(seconds, 0, -1):
        print(Fore.cyan +"| "+ str(i) + Style.RESET_ALL)
        time.sleep(1)

    print("| done")
