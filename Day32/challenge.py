import smtplib
import datetime as dt
import random

my_email = "wwaleedfadl@gmail.com"
password = "cgesweehvifzwuzl"

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
day_of_week = now.weekday()


# date_of_birth = dt.datetime(year=1997, month=5, day=19, hour=4)
# print(date_of_birth)

if day_of_week == 6:
    print("This is day 6")

    with open('quotes.txt') as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    print(quote)

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="wwaleedfadl@outlook.com",
            msg=f"Subject:Monday Motivation \n\n {quote}")
