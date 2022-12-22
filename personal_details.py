import pyodbc

def data():
    connect = pyodbc.connect('Driver={SQL Server};'
                             'Server=LAPTOP-PEJ2KCFH;'
                             'Database=Game;'
                             'Trusted_Connection=yes;')
    cursor = connect.cursor()

    PersonID = input("Please enter your ID: ")
    Full_name = input("Write your Full_name: ")
    Grade = input("Enter your Score? ")
    cursor.execute("INSERT INTO Game_table (PersonID, Full_name, Grade)"
                   "VALUES(?,?,?)", (PersonID, Full_name, Grade))
    connect.commit()
data()