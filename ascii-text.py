import pyfyglet

REQUIRES = ["pyfiglet"]

def run():
	print("\n== ASCII TEXT ==")
	textascii = input("| ecrit quelque chose... >")
	result = pyfiglet.figlet_format (textascii, font = "standard")
	print(result)
