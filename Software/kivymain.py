#!/usr/bin/python
#import sys
import threading
import gui
import uart_service1

def main():
	tasks = [gui.Main().run(),uart_service1.run()]
	for task in tasks:
		t = threading.Thread(target=task)
		t.start()

if __name__ == '__main__':
	main()
