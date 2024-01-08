import smtplib as s

ob=s.SMTP('smtp.gmail.com',587)
ob.ehlo()
ob.starttls()
ob.login('arpitpandit2017@gmail.com','"TRACKA2u3a@700029++**++282010"')
print("Login Successful")
Subject="hi ji"
body="I Love python"
message="subject:{}\n\n{}".format(Subject,body)
listadd=['us916543@gmail.com','panditarpitsharma82@gmail.com']
ob.sendmail('arpitpandit2017@gmail.com',listadd,message)
print("Email Sent")
ob.quit()