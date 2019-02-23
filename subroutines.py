import os
from random import randint
from getpass import getpass
from time import sleep

status = ['Nq', 'Nq', 'Kc', 'Kc', 'Kc', 'Dw']
locations = ['Ax', 'Fr', 'Je', 'Mv', 'Pn', 'Yb', 'Un', 'Bt']
suit = ['Rj', 'Em', 'Sb', 'Xp']
rank = ['Kq', 'Ze', 'At', 'Dd', 'Lu', 'Mp', 'Yw', 'Bn', 'Sb', 'Wk', 'Rv', 'Hy', 'Cr']

bad_status = ['Qn', 'Qn', 'Ck', 'Ck', 'Ck', 'Wd']
bad_locations = ['Xa', 'Rf', 'Ej', 'Vm', 'Np', 'By', 'Nu', 'Tb']
bad_suit = ['Jr', 'Me', 'Bs', 'Px']
bad_rank = ['Qk', 'Ez', 'Ta', 'Dd', 'Ul', 'Pm', 'Wy', 'Nb', 'Bs', 'Kw', 'Vr', 'Yh', 'Rc']

message = "01100100 01100101 01100001 01110100 01101000 01011111 01110100 01101111 01011111 01101110 01101001 01100010 01101001 01110010 01110101"


def code_gen():
    print("Performing system diagnostic.")
    sleep(0.5)
    print(".")
    sleep(0.5)
    print(".")
    sleep(0.5)
    print(".")
    sleep(0.5)
    print("Diagnostic code: 00.%s.%s.%s.%s" % (status[randint(0, 5)],
    locations[randint(0, 7)], suit[randint(0, 3)], rank[randint(0, 12)]))
    print("Complete maintenance as needed.")


def sid():
    os.system('clear')
    print("Activating Sid Corvin Protocol")
    sleep(1)
    print(".")
    sleep(1)
    print(".")
    sleep(1)
    print(".")
    sleep(1)
    print("So...")
    sleep(1)
    print("I am either dead or a rather angry, quite alive, me will be storming in right about...")
    sleep(3)
    print("NOW!")
    sleep(1)
    print("...")
    sleep(1)
    print("No?")
    sleep(3)
    print("Well. My condolences on your loss.")
    sleep(3)
    print("And please allow me the opportunity to pass along a final message:")
    sleep(5)
    print("During our long, hard journey from our previous predicaments, be it oppression,")
    sleep(2)
    print("enslavement, incarceration, or even extinction to the new lives we have carved out")
    sleep(2)
    print("for ourselves together in this universe of unknowns, it is easy to look back and see")
    sleep(2)
    print("the vast distances we have come physically and metaphorically together.")
    sleep(10)
    print("Knowing you bunch, y'all are staring down the barrel of something big.")
    sleep(2)
    print("So of course it's also easy to look forward and see what lies ahead and")
    sleep(2)
    print("the good that will ripple out from it.")
    sleep(10)
    print("But it’s not always easy, with all this lookin' back and forward...")
    sleep(3)
    print("to remember to look to our sides... ")
    sleep(3)
    print("to the people with us.")
    sleep(3)
    print("These amazing people who have traveled so far with us and will whole-heartedly")
    sleep(2)
    print("journey with us into the future.")
    sleep(2)
    print("Cherish the time when nothing is happening and share it with those who mean something to you. ")
    sleep(10)
    print("Oh. And Captain? Sid Corvin reporting for duty...")
    sleep(2)
    print("albeit in a slightly different uniform.")
    sleep(10)
    input('Press "Enter" to continue.')
    os.system('clear')
    print("RNS Revelation automated systems performing at 45% above normal efficiency.")
    sleep(5)
    input('Press "Enter" to continue.')
    os.system('clear')


def self_destruct():
    special_pass = "Zellosian1885red"
    abort = ''
    print("Initial passcode accepted.")
    passin = getpass("Enter clearance level-7 passcode to intialize self-destruct: ")
    if passin == special_pass:
        print("The RNS Revelation self-destruct sequence has been engaged.")
        print("Three minutes until self-destruction.")
        while abort != "abort":
            abort = input("")
    else:
        print("Incorrect passcode. Self-destruct sequence failed to initiate.")
        input("")
        return False


def lockout(cycle):
    escape = "death_to_nibiru"
    entry = ''
    os.system('clear')
    print("The current cycle number is: %s" % cycle)
    print("Is this correct? (Y/N) y")
    print("1. Run system diagnostic.")
    print("2. Change maintenance admin password.")
    print("3. Activate SCP")
    print("4. Initiate self-destruct sequence.")
    input("Choose a function from the menu above: ")
    for i in message:
        if i == '0':
            print('')
        elif i == '1':
            print('.')
            sleep(0.2)
    print("This is The Metatron. I have taken control of this console.")
    sleep(0.2)
    print("If you wish to restore access, you must transfer 10 commercial resources to the Confederacy.")
    sleep(0.2)
    print("You can wire these funds to the untraceable account at subspace frequency 32-mjz-155-mn.")
    sleep(0.2)
    print("Thank you for your cooperation.")
    sleep(0.2)
    while entry != escape:
        entry = input("Confederate Authorizaiton Required: ")
    os.system('clear')


def corrupt_code():
    print("Performing system diagnostic.")
    print("WARNING: Diagnostic protocol fault.")
    sleep(0.5)
    print(".")
    sleep(0.5)
    print(".")
    sleep(0.5)
    print(".")
    sleep(0.5)
    print("Diagnostic code: 00.%s.%s.%s.%s" % (bad_status[randint(0, 5)],
    bad_locations[randint(0, 7)], bad_suit[randint(0, 3)], bad_rank[randint(0, 12)]))
    print("Complete maintenance as needed.")
    print("Automated systems working to correct fault. No additional user action required.")
