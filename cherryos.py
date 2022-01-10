import os
import platform
p = platform.system()
profile = open("profile.cos", "r")
name = profile.read()

def clear():
    if (p == "Windows"):
        os.system("cls")
    else:
        os.system("clear")

def pfmaker():
    clear()
    name = input("Enter username: ")
    pfmake = open("profile.cos", "w")
    pfmake.write(name)
    reloadpf()
    pfmake.close()
    clear()
    input("Reload CherryOS for changes to take effect...\n\nPress enter to continue...")
    clear()
    menu()

def reloadpf():
    profile = open("profile.cos", "r")
    name = profile.read()

def run(path):
    path = "py {}".format(path)
    os.system(str(path))
    clear()
    menu()

def menu():
    i = input("CherryOS - Version 1.0.0\nWelcome back, {}!\n\nEnter command: ".format(name))
    if (i == "help"):
        clear()
        print("List of Commands\n\nhelp\nrun\nprofile\nexit")
        input("\nPress enter to continue...")
        clear()
        menu()
    elif (i == "run"):
        clear()
        path = input("Enter path (Type 'cancel' to go back.): ")
        if (path == "cancel"):
            clear()
            menu()
        else:
            clear()
            run(path)
    elif (i == "profile"):
        clear()
        i = input("Would you like to 'view' or 'make' your profile?\n")
        if (i == "view"):
            clear()
            reloadpf()
            print("Username: {}".format(name))
            input("\nPress enter to continue...")
            clear()
            menu()
        elif (i == "make"):
            pfmaker()
        else:
            clear()
            input("Invalid command...\n\nPress enter to continue...")
            clear()
            menu()
    elif (i == "exit"):
        clear()
        input("Thank you for using CherryOS!\nPress enter to exit...")
        exit()
    else:
        clear()
        input("Invalid command...\n\nPress enter to continue...")
        clear()
        menu()

clear()
menu()
