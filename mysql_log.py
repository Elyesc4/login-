import mysql.connector
import datetime
from datetime import date


class User:

    def __init__(self, full_name, birthday):
        self.name = full_name
        self.birthday = birthday

        name_pieces = full_name.split(" ")
        self.first_name = name_pieces[0]
        self.last_name = name_pieces[-1]

    def age(self):
        try:
            today = date.today()
            dd = int(self.birthday[0:2])
            mm = int(self.birthday[2:4])
            yyyy = int(self.birthday[4:8])
            dob = datetime.date(yyyy, mm, dd)
            age_in_days = (today - dob).days
            age_in_years = age_in_days / 365
            return int(age_in_years)
        except ValueError:
            print("This didn't worked check if you did it right ")


user_name1 = input("Enter your first Name: ")
user_name2 = input("Enter your last Name: ")
user_name = user_name1 + " " + user_name2
birthday = input("Enter your date of birth in ddmmyyyy format like this 01012010 = 1.1.2010: ")

user = User(user_name, birthday)

print("Welcome " + user_name1 + "!")

password = input("Now choose a password: ")

age = user.age()


cnx = mysql.connector.connect(
    user='root',
    password='Password',
    host='localhost',
    database="mydatabase"
)

my_cursor = cnx.cursor()

sql = "INSERT INTO users (1name, 2name, age, password) VALUES (%s, %s, %s, %s)"
val = (user_name1, user_name2, age, password)
my_cursor.execute(sql, val)

cnx.commit()

