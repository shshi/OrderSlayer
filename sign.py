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
        log_data = {'loginPhone':'18209347100','loginPassword':'ssh19198918'} #登录post数据
        sgn_data = {'translatorId':'WE16104633TR'} #签到post数据
        headers = {"Host":"talent.woordee.com", "Connection":"keep-alive", "Content-Length":"25",
                   "Accept":"*/*", "Origin":"http://talent.woordee.com", "X-Requested-With":"XMLHttpRequest",
                   "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36",
                   "Content-Type":"application/x-www-form-urlencoded",
                   "Referer":"http://talent.woordee.com/front/square",
                   "Accept-Encoding":"gzip, deflate",
                   "Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8",
                   "Cookie": "gr_user_id=5ada753b-6053-4862-992d-609e344b0097; UM_distinctid=162fd37c4ed35a-0f9b591b54436c-7b113d-130980-162fd37c4ee296; CNZZDATA1261954912=526383338-1505555533-%7C1529057341; WOORDEE_SID=8d5dd8df6dc4433f884e1fc8707f30c3"
                  }
    
        #登录操作
        log = s.post('http://talent.woordee.com/front/truser/login', log_data) #post登录地址 
        html = s.get('http://talent.woordee.com/front/square') #get登陆后的地址
        page_bf = html.content
        page_bf = page_bf.decode('utf-8')
        count_bf_re = re.compile(r'<em class="signedCount">(.*?)天</em>')
        count_bf = re.findall(count_bf_re, page_bf)
        count_bf = float(count_bf[0])
        print (count_bf)

        #签到操作
        s.post('http://talent.woordee.com/front/truser/sign', data=sgn_data, headers=headers) #触发签到  

        #提取签到结果并打印
        page_aft = s.get('http://talent.woordee.com/front/square').content #重新get地址并获取页面源码
        page_aft = page_bf.decode('utf-8')
        count_aft_re = re.compile(r'<em class="signedCount">(.*?)天</em>')
        count_aft = re.findall(count_aft_re, page_aft)
        count_aft = float(count_aft[0])
        print (count_aft)
        print (count_bf+1)
        if count_aft == count_bf+1 and count_aft>300:
            print ("Successfully signed")
        else:
            sendMail()
        
        #page=page.decode('utf-8')
        #style_re = re.compile(r'id="nSign"  style="(.*?)">')
        #style = re.findall(style_re, page_aft)
        #print (page)
        #print (style)
        #if "none" in style[0]:
            #print ("Successfully signed")
        #else:
            #sendMail()
    except Exception as e:
        print (e)
        sendMail()

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
