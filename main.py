# Head operation for auto installer
try:
    import os as s
except ModuleNotFoundError():
    print(
        "Module Named 'os' not found, Kindly install it by typing 'python -m pip install os -y' on your terminal"
    )
    exit()


# Terminal Cleaner
def C():
    if s.name == "posix":
        s.system('clear')
    else:
        s.system('cls')


# python module/package auto installer
try:
    import requests
    from colorama import Fore
except ModuleNotFoundError:
    try:
        C()
        print(
            "Missing required modules detected\nPlease note!!! Internet connection is required for this automatic module installer to work properly!!!"
        )
        print("Attempting to install module named requests")
        s.system("python -m pip install requests -y")
        print("Attempting to install module named colorama")
        s.system("python -m pip install colorama -y")
        print(
            "Operation Completed, Exiting...\nPlease open this script manually"
        )
        exit()
    except KeyboardInterrupt():
        print("Operation Killed")
        exit()

try:
    C()
    print(Fore.RED + """
▄▀█ █▀▄ █▀▄▀█ █ █▄░█ ▄▄ █▀▀
█▀█ █▄▀ █░▀░█ █ █░▀█ ░░ █▀░
\n""")
    print(Fore.GREEN + "Coded By: " + Fore.RED + "Bl4ckphoenix")
    print(Fore.GREEN + "In Collaboration With: " + Fore.RED + " RedFurrFox")
    print(
        Fore.GREEN + "Join Our Group:" + Fore.RED +
        " Android Hacker PH\n\n"
    )

    web = input(Fore.BLUE + 'URL: ')
    with open("admin_wordlist.txt", "r") as a_file:
        for line in a_file:
            stripped_line = line.strip()
            req = str(web) + stripped_line
            che = requests.post(req)
            if che.status_code == 200:
                print(
                    f'\033[1;32;40m[✔] Code = {che.status_code}, Site = {req}')
            if che.status_code == 400:
                print(
                    f'\033[1;31;40m[X] Code = {che.status_code}, Site = {req}')
            elif che.status_code == 404:
                print(
                    f'\033[1;31;40m[X] Code = {che.status_code}, Site = {req}')
            else:
                print(
                    f'\033[1;31;40m[X] Code = {che.status_code}, Site = {req}')
except KeyboardInterrupt:
    print(Fore.RED + "\n\nProgram Has Been Stop Thanks For Using Our Tool...")
except ValueError:
    print()
except TypeError:
    print()
except EOFError:
    exit()
