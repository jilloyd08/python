import smtplib
from email.message import EmailMessage

email = EmailMessage()
email["from"] = "Neo Matrix"
email["to"] = " " # insert recipient email.
email["subject"] = "You won $1,000!"

email.set_content("I am a Python Master!")

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login("# enter sender email", "# enter sender pass")
	smtp.send_message(email)
	print("all good boss")