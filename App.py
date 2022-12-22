from Utility import *
from colorama import Fore


class Game:
    print(Fore.GREEN, "\n\t\t\t\t\t\t\t**************** Welcome To Trivia Game **************** \n", Fore.RESET)
    print(Fore.YELLOW, "\t\t\t\t1.Biology", "\t\t\t\t2.Geography", "\t\t\t\t3.Sport\n", Fore.RESET)
    # insert = input(f"{Fore.CYAN}Choose one of them:{Fore.RESET} ")
    while True:
        insert = input(f"{Fore.CYAN}Choose one of them:{Fore.RESET} ")
        if insert == "1":
            t = Biology()
            t.biology()
            # cont = input("Do you went to Continue y/n: ")
            # while cont == "y":
            #     continue
            # else:
            #     exit()
        elif insert == "2":
            i = Geography()
            i.geography()
        elif insert == "3":
            v = Sport()
            v.sport()
        cont = input("Do you went to Continue y/n: ")
        while cont == "no":
            exit()
