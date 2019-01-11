#-*- coding: utf-8 -*-
#===========================================================
# Author：Sha0hua
# E-mail:shi.sh@foxmail.com
# Modified Date: 2019-01-11
#===========================================================
import re
import urllib
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def DUcheck():
    try:
        url="http://www.dali.edu.cn/nrsc/gkzp/index.htm"
        page = urllib.request.urlopen(url)
        html = page.read()
        reg = r'<a href="(.*?)" title="(?:(?!视频|词汇).)*?" target="_blank">.*?</a>'
        reg = r'<span>(.*?)</span>'#<span>2018-06-13</span>
        date_re = re.compile(reg)
        date_list = re.findall(date_re,html)
        latest = date_list[0]
        #print date_list
        #print latest
        #print type(latest)

        if latest == "2018-06-13":
            print ("no update")
        else:
            print ("new update! %s"%latest)
            sendMail()
            
    except Exception as e:
        print (e)
        sendMail_error()

def sendMail():        
    msg = MIMEMultipart()
    body = MIMEText("New update!\nPlease visit http://www.dali.edu.cn/nrsc/gkzp/index.htm")
    msg.attach(body)
    msg['Subject'] = 'New update on Dali University website!'
    msg['From'] = "sign.Heroku<cell.fantasy@qq.com>"
    msg['To'] = "shi.sh@foxmail.com"
    try:
        s = smtplib.SMTP_SSL("smtp.qq.com", 465)
        s.connect("smtp.qq.com")
        s.login("cell.fantasy","Ssh31415926")
        s.sendmail("sign.Heroku<cell.fantasy@qq.com>", "shi.sh@foxmail.com", msg.as_string())
        s.close()
        print ("Successfully sent to %s"%msg['to'])
    except Exception as e:
        print (e)

def sendMail_error():        
    print ("Failed in checking update")
    msg = MIMEMultipart()
    body = MIMEText("ERROR happened from checking update on Dali University website, please check on Heroku immediately!")
    msg.attach(body)
    msg['Subject'] = 'ERROR happened from checking update!'
    msg['From'] = "sign.Heroku<cell.fantasy@qq.com>"
    msg['To'] = "shi.sh@foxmail.com"
    try:
        s = smtplib.SMTP_SSL("smtp.qq.com", 465)
        s.connect("smtp.qq.com")
        s.login("cell.fantasy","Ssh31415926")
        s.sendmail("sign.Heroku<cell.fantasy@qq.com>", "shi.sh@foxmail.com", msg.as_string())
        s.close()
        print ("Successfully sent to %s"%msg['to'])
    except Exception as e:
        print (e)
    
DUcheck()
