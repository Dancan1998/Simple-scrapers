import smtplib
from bs4 import BeautifulSoup
import requests
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from decouple import config

def sendMailFunc(mail_content, subject, receiver_address):
    sender_address = 'dancanchibole8@gmail.com'
    sender_pass= config('sender_pass')
    message = MIMEMultipart()
    link = url
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = subject
    message.attach(MIMEText(mail_content, 'plain'))
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    session.login(sender_address, sender_pass)
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print("Mail sent")
    

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}
url = "https://www.jumia.co.ke/hp-display-monitor-24fw-23.8-ultra-slim-with-dual-33371902.html"

req = requests.get(url, headers=header)
soup = BeautifulSoup(req.content, 'html.parser')
title = soup.find("h1", {"class": "-fs20"}).text
current_price = soup.find("span", {"class": "-b"}).text.split()[1]
current_price_updated = list(current_price)
newlist = []
for value in current_price_updated:
    # print(value)
    if value == ',':
        # print("Convert string to integer by removing the integer")
        pass
    else:
        newlist.append(value)
productPrice = ''.join(newlist)
finalPrice = int(productPrice)
if finalPrice <= 25000:
    # print("Current price for {} is affordable at Kshs {}".format(title, finalPrice))
    sendMailFunc("Hello Dancan, New Price!! Current price for {} is affordable at Kshs {}. Click on the link if still interested {}".format(title, finalPrice, url),\
        "New Price Out Dancan",\
        "dancankingstar@gmail.com",\
        )
elif finalPrice > 25001:
    print("Current price for {} is affordable at Kshs {}".format(title, finalPrice))
