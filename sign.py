# -*- coding:utf-8 -*-
#===========================================================
# Author：Sha0hua
# E-mail:shi.sh@foxmail.com
# Created Date: 2017-09-07
# Modified Date: 2017-09-19
# Version: 2.0
# Description: sign at Woordee website  
#===========================================================
import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def sign():
    try:
        #登录及签到post数据准备
        s = requests.session()
        log_data = {'loginPhone':'18209347100','loginPassword':'ssh19198918'} #登录post数据
        sgn_data = {'translatorId':'WE16104633TR'} #签到post数据
    
        #登录操作
        log = s.post('http://talent.woordee.com/front/truser/login', log_data) #post登录地址 
        html = s.get('http://talent.woordee.com/front/square') #get登陆后的地址        

        #签到操作
        s.post('http://talent.woordee.com/front/truser/sign', sgn_data) #触发签到  

        #提取签到结果并打印
        page = s.get('http://talent.woordee.com/front/square').content #重新get地址并获取页面源码
        soup = BeautifulSoup(page,"html.parser")

        txt1 = soup.find_all('a', attrs={"id":"ySign"})[0].get_text().strip() #提取“已签到”文本
        #txt2 = soup.find_all('em', attrs={"class":"signedCount"})[0].get_text() #提取“连续签到n天”文本
        print (txt1)
        if len(txt1)==3:
            print ("Successfully signed")
        else:
            sendMail()
    except:
        sendMail()

def sendMail():        
    print ("Signing ERROR")
    msg = MIMEMultipart()
    body = MIMEText("ERROR happened from running sign.py, please check on Heroku immediately!")
    msg.attach(body)
    msg['Subject'] = 'ERROR happened from running sign.py on Heroku!'
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
    
sign()
