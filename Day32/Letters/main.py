import smtplib
import datetime as dt
import pandas

my_email = "wwaleedfadl@gmail.com"
password = "cgesweehvifzwuzl"

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
day_of_week = now.weekday()

today = (month, day)

data = pandas.read_csv('birthday.csv')

birthday_dict = {
    (month, day): data_row
}

new_dict = {(data_row['month'], data_row['day']): for (index, data_row) in data.iterrows()}

with open('birthdays.csv') as dates_file:
    birth_dates = dates_file.readlines()
print(birth_dates)
