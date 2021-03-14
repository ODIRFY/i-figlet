#!/usr/bin/python3
import os

# Please use Linux

if os.system('figlet -v 2>&1 > /dev/null') == 32512:
	os.system('clear')
	print("\n\n\nFiglet is not installed!\n\n\n")
	exit()

if os.system('lolcat --version 2>&1 > /dev/null') == 32512:
	os.system('clear')
	print("\n\n\nLolcat is not installed!\n\n\n")
	exit()

os.system('clear')
txt = input('Enter text here: ')

while True:
	os.system('clear')
	print("\n"*10)
	os.system("" + 'figlet -c "{}" | lolcat' .format(txt))
	txt = input(" ")
	
	if txt == 'q':
		print("\nExit")
		break