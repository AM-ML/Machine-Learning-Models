from time import sleep
from subprocess import call
from random import randint
from sys import exit
from cowsay import tux


global_counter = 0

def line(ctr):
	for i in range(1, 30):
		print(f"$*/2{ctr*(randint(1, 103)/randint(1, 30))}", end="")
	print()


def func():
	counter = 0
	breaker = int(200*(randint(1, 10)/randint(1,100)))

	while(True):
		breaker = int(200*(randint(1, 3)/randint(1,10)))
		sleep(0.01)
		if counter % breaker == 0:
			call("cls", shell=True)
			sleep(0.04)
		line(counter)
		counter+=1

def main():
	try:
		func()
	except KeyboardInterrupt:
		call("cls", shell=True)
		sleep(0.1)
		message = "DATA BREACH SUCCESSFUL!"
		tux(message)
		exit(0)

if __name__ == '__main__':
	main()