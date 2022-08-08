import smtplib

my_email = "kdstar008@gmail.com"
password = "JsonClass12#"
connection = smtplib.SMTP("smtp.gmail.com")

connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs="selflessmonk54@gmail.com", msg="Hello Friend")
connection.close()