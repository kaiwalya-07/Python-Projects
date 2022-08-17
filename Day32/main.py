import smtplib

my_email = "type email"
password = "Type password"
connection = smtplib.SMTP("smtp.gmail.com")

connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs="selflessmonk54@gmail.com", msg="Hello Friend")
connection.close()
