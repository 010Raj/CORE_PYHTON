import smtplib
import traceback

gmail_user = 'rajgeru84@gmail.com'
gmail_password = 'xelt wfxc xcfg abgx'

sent_from = gmail_user
to = ['aniketsirota64@gmail.com']
subject = 'this is my first python Message'
body = 'Hi! user please click on this link to buy and order it online! \n https://www.flipkart.com/'

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.ehlo()
    server.login(gmail_user,gmail_password)
    server.sendmail(sent_from,to,body)
    server.close()
    print('Email Sent!')

except:
    traceback.print_exc()

