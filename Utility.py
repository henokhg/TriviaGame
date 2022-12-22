import pyodbc
from colorama import Fore


class Biology:

    def biology(self):
        SQL = pyodbc.connect('Driver={SQL Server};'
                             'Server=LAPTOP-PEJ2KCFH;'
                             'Database=Trivia_Game;'
                             'Trusted_Connection=yes;')
        biology = 'select Question, A, B, C, D, Answer from Biology'
        cursor = SQL.cursor()
        cursor.execute(biology)
        score = 0
        for choice in cursor:
            print(choice[0])
            print(choice[1])
            print(choice[2])
            print(choice[3])
            print(choice[4])
            answer = input("choice one of them: ")
            if answer == choice[5]:
                score += 1
            print(Fore.LIGHTBLUE_EX, "you got ", str(score), "/", "5", "correct", Fore.RESET)


class Geography(Biology):

    def geography(self):
        SQL = pyodbc.connect('Driver={SQL Server};'
                             'Server=LAPTOP-PEJ2KCFH;'
                             'Database=Trivia_Game;'
                             'Trusted_Connection=yes;')
        biology = 'select Question, A, B, C, D, Answer from Geography'
        cursor = SQL.cursor()
        cursor.execute(biology)
        score = 0
        for choice in cursor:
            print(choice[0])
            print(choice[1])
            print(choice[2])
            print(choice[3])
            print(choice[4])
            answer = input("choice one of them: ")
            if answer == choice[5]:
                score += 1
            print(Fore.LIGHTBLUE_EX, "you got ", str(score), "/", "5", "correct", Fore.RESET)


class Sport(Geography):

    def sport(self):
        SQL = pyodbc.connect('Driver={SQL Server};'
                             'Server=LAPTOP-PEJ2KCFH;'
                             'Database=Trivia_Game;'
                             'Trusted_Connection=yes;')
        biology = 'select Question, A, B, C, D, Answer from Sport'
        cursor = SQL.cursor()
        cursor.execute(biology)
        score = 0
        for choice in cursor:
            print(choice[0])
            print(choice[1])
            print(choice[2])
            print(choice[3])
            print(choice[4])
            answer = input("choice one of them: ")
            if answer == choice[5]:
                score += 1
            print(Fore.LIGHTBLUE_EX, "you got ", str(score), "/", "5", "correct", Fore.RESET)


