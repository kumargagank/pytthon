



import smtplib

s=smtplib.SMTP('smtp.gmail.com','587')
s.starttls()
receiver='harshitarkumbar22@gmail.com'
sender='gaganmsdhonikumar@gmail.com'
msg="hii"
s.login(sender,'********')
s.sendmail(sender,receiver,msg)
print("msg sent successfully")
s.quit()