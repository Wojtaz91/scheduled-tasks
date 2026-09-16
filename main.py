import datetime as dt
import smtplib
import pandas as pd
import random
my_email = "wojciechturalski91@gmail.com"
my_password = "jprfvrhhogifkbdg"
serwer = "smtp.gmail.com"
today = (dt.datetime.now().month, dt.datetime.now().day)
# print(today)


data = pd.read_csv("birthdays.csv")
# ? cos for cos in cos gdzie pierwsze cos to key"value
# birthday_dict = {}
#
# for (index, data_row) in data.iterrows():
#     birthday_dict[(data_row.month, data_row.day)] = data_row  ----> rozbudowana wersja tego nizej
birthday_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

if today in birthday_dict:
    person = birthday_dict[today]
    # print(person)
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as f:
        contents = f.read()
        contents = contents.replace("[NAME]", person["name"])
        contents = contents.replace("Angela", "Wojciech")
        print(person["name"])
        print(contents)

    with smtplib.SMTP(serwer) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=person["email"],
            msg=f"Subject: Wszystkiego najlepszego!\n\n{contents}",)

# 4. Send the letter generated in step 3 to that person's email address.
# HINT 1: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
# HINT 2: Remember to call .starttls()
# HINT 3: Remember to login to your email service with email/password. Make sure your security setting is set to allow less secure apps.
# HINT 4: The message should have the Subject: Happy Birthday then after \n\n The Message Body.



