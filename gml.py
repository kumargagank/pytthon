



import smtplib

s=smtplib.SMTP('smtp.gmail.com','587')
s.starttls()
receiver='gagangana9739@gmail.com'
sender='gaganmsdhonikumar@gmail.com'
msg="hii"
s.login(sender,'89456123')
s.sendmail(sender,receiver,msg)
print("msg sent successfully")
s.quit()