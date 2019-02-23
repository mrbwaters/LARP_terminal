import os
import subroutines
from getpass import getpass
from time import sleep

def interface(cycle, passcode):
    if cycle == 0:
        print("Cycle number error.")
        input('')
        return passcode
    else:
        while True:
            print("1. Run system diagnostic.")
            print("2. Change maintenance admin password.")
            print("3. Activate SCP")
            print("4. Initiate self-destruct sequence.")
            choice = input("Choose a function from the menu above: ")
            if choice == '1':
                if cycle > 10 and cycle < 14:
                    subroutines.corrupt_code()
                    passin = getpass("Enter passcode to advance to next cycle: ")
                    while passin != passcode:
                        passin = getpass("Unathorized passcode. Try again: ")
                    return passcode
                else:
                    subroutines.code_gen()
                    passin = getpass("Enter passcode to advance to next cycle: ")
                    while passin != passcode:
                        passin = getpass("Unathorized passcode. Try again: ")
                    return passcode
            elif choice == '2':
                passin = getpass("Enter current passcode: ")
                if passin == passcode:
                    passcode = getpass("Create new admin passcode: ")
                else:
                    print("Incorrect passcode.")
                    input('Press "Enter" to continue.')
                    os.system('clear')
            elif choice == '3':
                print("Hi there. I'm afraid I am going to have to ask you for a special authorization code.")
                passin = input("Enter SCP authorization: ")
                if passin == 'Th3L0ngH4rdR04dT0P34c3':
                    subroutines.sid()
                else:
                    print("Sorry about that but you don't have the right code.")
                    input('Press "Enter" to continue.')
                    os.system('clear')
            elif choice == '4':
                passin = getpass("Enter passcode to engage self-destruct sequence: ")
                if passin == passcode:
                    subroutines.self_destruct()
                else:
                    print("Incorrect passcode.")
                    input('Press "Enter" to continue.')
                    os.system('clear')
            else:
                print("Invalid input.")
                input('Press "Enter" to continue.')
                os.system('clear')
