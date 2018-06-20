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
import re
#from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def sign():
    try:
        #登录及签到post数据准备
        s = requests.session()
        headers_login = {"Host":"talent.woordee.com", "Connection":"keep-alive", "Content-Length":"125",
                   "Accept":"*/*", "Origin":"http://talent.woordee.com", "X-Requested-With":"XMLHttpRequest",
                   "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36",
                   "Content-Type":"application/x-www-form-urlencoded",
                   "Referer":"http://talent.woordee.com/front/truser.html",
                   "Accept-Encoding":"gzip, deflate",
                   "Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8",
                   "Cookie": "gr_user_id=5ada753b-6053-4862-992d-609e344b0097; UM_distinctid=162fd37c4ed35a-0f9b591b54436c-7b113d-130980-162fd37c4ee296; CNZZDATA1261954912=526383338-1505555533-%7C1529417456; WOORDEE_SID=c79c457e7b054ef88b691f8d236752d3"
                  }
        login_data = {'loginPhone':'18209347100','loginPassword':'11221135d35eacd2de7b136d15be0662','loginLowerCasePassword':'11221135d35eacd2de7b136d15be0662'} #登录post数据
        
        headers_sign = {"Host":"talent.woordee.com", "Connection":"keep-alive", "Content-Length":"25",
                   "Accept":"*/*", "Origin":"http://talent.woordee.com", "X-Requested-With":"XMLHttpRequest",
                   "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36",
                   "Content-Type":"application/x-www-form-urlencoded",
                   "Referer":"http://talent.woordee.com/front/square",
                   "Accept-Encoding":"gzip, deflate",
                   "Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8",
                   "Cookie": "gr_user_id=5ada753b-6053-4862-992d-609e344b0097; UM_distinctid=162fd37c4ed35a-0f9b591b54436c-7b113d-130980-162fd37c4ee296; CNZZDATA1261954912=526383338-1505555533-%7C1529057341; WOORDEE_SID=8d5dd8df6dc4433f884e1fc8707f30c3"
                  }
        sign_data = {'translatorId':'WE16104633TR'} #签到post数据
        headers_square = {"Host":"talent.woordee.com", "Connection":"keep-alive", "Upgrade-Insecure-Requests":"1",
                   "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36",
                    "X-Requested-With": "XMLHttpRequest",
                   "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                   "Referer":"http://talent.woordee.com/front/truser/userCenter",
                   "Accept-Encoding":"gzip, deflate",
                   "Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8",
                   "Cookie": "gr_user_id=5ada753b-6053-4862-992d-609e344b0097; UM_distinctid=162fd37c4ed35a-0f9b591b54436c-7b113d-130980-162fd37c4ee296; CNZZDATA1261954912=526383338-1505555533-%7C1529417456; WOORDEE_SID=c79c457e7b054ef88b691f8d236752d3"
                  }
    
        #登录操作
        log = s.post('http://talent.woordee.com/front/truser/login', data=login_data, headers=headers_login) #post登录地址 
        html = s.get('http://talent.woordee.com/front/square', headers=headers_square) #get登陆后的地址

        #签到操作
        #s.post('http://talent.woordee.com/front/truser/sign', data=sign_data, headers=headers_sign) #触发签到  
        print ("Yes!")

        #提取签到结果并打印
        page = s.get('http://talent.woordee.com/getSignData', headers=headers_square).content #重新get地址并获取页面源码
        print (page)
        print (type(page))
        stringed=page.decode() 
        dic=eval(stringed)
        print (dic)
        print (dic["hasSigned"])
        print (dic["signedCount"])
    except Exception as e:
        print (e)
        #sendMail()

def sendMail():        
    print ("Failed in signing")
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
