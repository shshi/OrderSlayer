# -*- coding:utf-8 -*-
#===========================================================
# Name: WEsign
# Author：Sha0hua
# E-mail:shi.sh@foxmail.com
# Created Date: 2017-09-07
# Modified Date: 2017-09-08
# Version: 1.0
# Description: sign at Woordee website  
#===========================================================
import requests
from bs4 import BeautifulSoup
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def sign():

    #登录及签到post数据准备
    s = requests.session()
    log_data = {'loginPhone':'18209347100','loginPassword':'ssh19198918'} #登录post数据
    sgn_data = {'translatorId':'WE16104633TR'} #签到post数据
    
    #登录操作
    log = s.post('http://talent.woordee.com/front/truser/login', log_data) #post登录地址 
    html = s.get('http://talent.woord.com/front/truser/userCenter') #get登陆后的地址

    #签到操作
    s.post('http://talent.woordee.com/front/truser/sign', sgn_data) #触发签到  

    #提取签到结果并打印
    page = s.get('http://talent.woord.com/front/truser/userCenter').content #重新get地址并获取页面源码
    soup = BeautifulSoup(page,"html.parser")
    try:
        txt1 = soup.find_all('a', attrs={"class":"btn-sign"})[0].get_text() #提取“已签到”文本
        txt2 = soup.find_all('p', attrs={"class":"p2"})[0].get_text() #提取“连续签到n天”文本
        print (txt1+', '+txt2)
    except:
        print ("ERROR")
        msg = MIMEMultipart()
        body = MIMEText("ERROR happened from running WEsign.py, please check on Heroku immediately!")
        msg.attach(body)
        msg['Subject'] = 'ERROR happened from running WEsign.py on Heroku!'
        msg['From'] = "WEsign.Heroku<cell.fantasy@qq.com>"
        msg['To'] = "shi.sh@foxmail.com"
        try:
            s = smtplib.SMTP_SSL("smtp.qq.com", 465)
            s.connect("smtp.qq.com")
            s.login("cell.fantasy","Ssh31415926")
            s.sendmail("WEsign_Heroku<cell.fantasy@qq.com>", "shi.sh@foxmail.com", msg.as_string())
            s.close()
            print ("Successfully sent to %s"%msg['to'])
            return True
        except Exception as e:
            print (e)
            return False
    
sign()
time.sleep(3)
