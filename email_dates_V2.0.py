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
dates_dict = {dates[i]: occasions[i].strip() for i in range(len(occasions))}

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
		

		special_date = datetime.strftime(date, '%Y-%m-%d')
		
		# print(f'The special day is {dates_dict[special_date]}')
		

		email_address = os.environ.get('YourCustomEnvVar')
		email_password = os.environ.get('YourCustomEnvVar')


		msg = EmailMessage()
		msg['Subject'] = 'An Important Day Is Nigh'
		msg['From'] = email_address
		msg['To'] = youremail@address.com
		msg.set_content(f'Seany, \n{special_date} is a very important date! I hope you are ready to celebrate {dates_dict[special_date]}!')


		with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
			smtp.login(email_address, email_password)
			
			smtp.send_message(msg)

