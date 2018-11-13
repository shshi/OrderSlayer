#-*- coding: utf-8 -*-
#===========================================================
# Author：Sha0hua
# E-mail:shi.sh@foxmail.com
# Modified Date: 2018-06-15
# Version: 3.3
# Version Description: added switch sate check
#===========================================================
import re
import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def sign():
    try:
        s = requests.session()        
        headers_login = {"Host":"talent.woordee.com", "Connection":"keep-alive", "Content-Length":"125",
                   "Accept":"*/*", "Origin":"https://talent.woordee.com", "X-Requested-With":"XMLHttpRequest",
                   "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36",
                   "Content-Type":"application/x-www-form-urlencoded",
                   "Referer":"https://talent.woordee.com/users/login",
                   "Accept-Encoding":"gzip, deflate",
                   "Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8",
                   "Cookie": "_uab_collina=154185957300652152941643; gr_user_id=5e199aa3-38b1-49c3-977a-6b1f6bba8187; SESSION=d56a41a1-2ed2-4cb9-ac74-9586302f7496"
                  }
        login_data = {'loginPhone':'18209347100','loginPassword':'11221135d35eacd2de7b136d15be0662','loginLowerCasePassword':'11221135d35eacd2de7b136d15be0662'} #ç»å½postæ°æ®        
        headers_sign = {"Host":"talent.woordee.com", "Connection":"keep-alive", "Content-Length":"0",
                   "Accept":"*/*", "Origin":"https://talent.woordee.com", "X-Requested-With":"XMLHttpRequest",
                   "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36",
                   "Content-Type":"application/x-www-form-urlencoded",
                   "Referer":"https://talent.woordee.com/square/center",
                   "Accept-Encoding":"gzip, deflate",
                   "Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8",
                   "Cookie": "gr_user_id=5e199aa3-38b1-49c3-977a-6b1f6bba8187; SESSION=d56a41a1-2ed2-4cb9-ac74-9586302f7496"
                  }
        sign_data = {'translatorId':'WE16104633TR'}       
        headers_square = {"Host":"talent.woordee.com", "Connection":"keep-alive", "Accept": "*/*",
                   "X-Requested-With": "XMLHttpRequest",
                   "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
                   "Referer":"https://talent.woordee.com/square/center",
                   "Accept-Encoding":"gzip, deflate, br",
                   "Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8",
                   "Cookie": "SESSION=d56a41a1-2ed2-4cb9-ac74-9586302f7496; JSESSIONID=BC08F41F030CDA8A4670869DD7508F07"
                  }
    
        #ç»å½æä½
        log = s.post('https://talent.woordee.com/users/doLogin', data=login_data, headers=headers_login) #
        
        #ç­¾å°åæ°æ®è·å
        print ("logged in")
        
        #Check continous count of signed days
        content=requests.get('https://talent.woordee.com/message/unread/count', headers=headers_square).content
        print (content)
        #countBf=re.compile(r'id="continuousCount">(.*?)</em>')
        #countBf=re.findall(countBf, content)[0]
        #countBf=int(countBf)
        #print (countBf)
        
        #ç­¾å°æä½
        #s.post('https://talent.woordee.com/checkLogin', headers=headers_sign)
        #s.post('https://talent.woordee.com/square/operate/signdetail', headers=headers_sign)
        #s.post('https://talent.woordee.com/checkLogin', headers=headers_sign)
        s.post('https://talent.woordee.com/square/operate/sign', headers=headers_sign) #è§¦åç­¾å°  
        print ("Yes!")
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
