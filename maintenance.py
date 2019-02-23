import os
import subroutines
from interface import interface
from getpass import getpass
from time import sleep

cycle = 1
new_cycle = ''
correct_cycle = ''

os.system('clear')
print("Initializing RNS Revelation Maintenance Terminal")
sleep(0.5)
print(".")
sleep(0.5)
print(".")
sleep(0.5)
print(".")
sleep(0.5)
print("Please create a secure admin passcode for Maintenance Terminal.")
passcode = getpass('Passcode: ')

while True:
    os.system('clear')
    print("The current cycle number is: %s" % cycle)
    correct_cycle = input("Is this correct? (Y/N) ")
    if correct_cycle == 'Y' or correct_cycle == 'y':
        passcode = interface(cycle, passcode)
        cycle += 1
    elif correct_cycle == 'N' or correct_cycle == 'n':
        new_cycle = input("Please input correct cycle number: ")
        while not new_cycle.isdigit():
            print("Invalid input. Cycle number must be a positive integer.")
            new_cycle = input("Please input correct cycle number: ")
        passin = getpass("Enter passcode to alter cycle number: ")
        while passin != passcode:
            passin = getpass("Unathorized passcode. Try again: ")
        cycle = int(new_cycle)
    elif correct_cycle == 'lockout':
        subroutines.lockout(cycle)
    elif correct_cycle == 'special':
        os.system('clear')
        input('')
    elif correct_cycle == 'quit':
        break
    else:
        print("Invalid input. Enter 'Y' or 'N'.")
        input('')
