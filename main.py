import time
import re
import urllib2
import smtplib
from email.mime.text import MIMEText


#use the sina stock api to get the current price of stock
def get_price(id):
    url = "https://hq.sinajs.cn/list="
    request = urllib2.Request(url + id)
    request.add_header('Content-Type', 'application/json')
    response = urllib2.urlopen(request)
    data = response.read()                  #process the response data
    regroup = re.match(r'^var.*="(.*)"', data)
    data_string = regroup.group(1)
    obj = data_string.split(',')            #get some parameter of this stock
    price = obj[3]
    return price

def send_Email(message):
    mail_host = 'smtp.163.com'
    mail_user = 'XXX'           #set user name of your mail server
    mail_pass = 'XXX'           #set user password of your mail server


    sender = 'Stock Monitor'    #set the name of sender
    receivers = ['XXX']         #set the email address of receivers

    message = MIMEText(message, 'plain', 'utf-8')
    message['Subject'] = 'The main stock indexes of the Shanghai and Shenzhen stock markets have exceeded the set value'
    message['From'] = sender
    message['To'] = receivers[0]

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(
            sender, receivers, message.as_string())
        smtpObj.quit()
        print('Send E-mail finished')
    except smtplib.SMTPException as e:
        print('Error E-mail!!!', e)

monitor_list = "monitor_list.txt"
lines = open(monitor_list).read().splitlines()
stock_list = {}

# build the stock monitor list from stock list
for l in lines:
    cur = l.split()
    id = cur[0]
    price_obj = float(cur[1])
    stock_list[id] = price_obj

print ("Build stock list finished")

while True:
    for s in stock_list.keys():

        price_cur = float(get_price(s))
        price_obj = stock_list[s]

        if price_cur <= price_obj:
            message = "The main stock indexes of the Shanghai and Shenzhen stock markets have exceeded the set value.\n"
            message += "The current index price of " + s +' is '+ str(price_cur)
            message += "\nThe objective index price of " + s +' is '+str(price_obj)
            send_Email(message)
            exit()
    time.sleep(60)