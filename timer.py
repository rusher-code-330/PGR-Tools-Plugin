import time

def run():
    seconds = int(input("| time ?> "))

    for i in range(seconds, 0, -1):
        print(i)
        time.sleep(1)

    print("| done")