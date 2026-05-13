import pyfiglet


def run():
    print("\n== ASCII TEXT ==")

    textascii = input("| write something... > ")

    result = pyfiglet.figlet_format(textascii, font="standard")

    print(result)
