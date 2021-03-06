from datetime import timedelta, date, datetime
import csv
import os
import smtplib
from email.message import EmailMessage

# reading in csv file and adding data to empty lists
header = []
rows = []
occasions = []
dates = []
with open('date_book.csv', 'r', encoding='utf-8-sig') as f:
	date_reader = csv.reader(f, delimiter=',')
	header = next(date_reader)
	for row in date_reader:
		date = row[1]
		dates.append(date)
		occasion = row[0]
		occasions.append(occasion)

# making a dictionary just because
dates_dict = {occasions[i]: dates[i] for i in range(len(occasions))}

# get today's date
today = datetime.today().date()
# get a a week in advance
delta = timedelta(days=7)


advance = str(today + delta)
today_str = str(today)


# ***FIXME***
# figure out how to compare month and day ONLY

# compare today's date and a week ahead to the dates of special occasions
for date in dates:
	date = datetime.strptime(date, '%Y-%m-%d').date()
	date_to_string = str(date)
	if advance[4:] == date_to_string[4:] or today_str[4:] == date_to_string[4:]:
		# print('yes')

		special_date = datetime.strftime(date, '%Y-%m-%d')
		

		email_address = os.environ.get('PYTHON_EMAIL')
		email_password = os.environ.get('PYTHON_PASS')


		with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
			smtp.ehlo()
			smtp.starttls()
			smtp.ehlo()

			smtp.login(email_address, email_password)


			subject = 'Heyo!'
			body = f'Seany,',special_date, 'is a very important date!'

			msg = f'Subject: {subject}\n\n{body}'

			smtp.sendmail(email_address, 'seanfaubus@gmail.com', msg)

