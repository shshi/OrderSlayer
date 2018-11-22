#-*- coding: utf-8 -*-
#===========================================================
# Author：Sha0hua
# E-mail:shi.sh@foxmail.com
# Modified Date: 2018-11-15
#===========================================================
import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def sign():
    try:
        s = requests.session()
        headers_resp = {"Host":"talent.woordee.com", "Connection":"keep-alive", "Cache-Control":"max-age=0",
                   "Upgrade-Insecure-Requests":"1", "Origin":"https://talent.woordee.com", "X-Requested-With":"XMLHttpRequest",
                   "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36",
                   "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                   "Accept-Encoding":"gzip, deflate, br",
                   "Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8"
                  }
        headers_login = {"Host":"talent.woordee.com", "Connection":"keep-alive", "Content-Length":"125",
                   "Accept":"*/*", "Origin":"https://talent.woordee.com", "X-Requested-With":"XMLHttpRequest",
                   "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36",
                   "Content-Type":"application/x-www-form-urlencoded",
                   "Referer":"https://talent.woordee.com/users/login",
                   "Accept-Encoding":"gzip, deflate, br",
                   "Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8"
                  }
        login_data = {'loginPhone':'18209347100','loginPassword':'11221135d35eacd2de7b136d15be0662','loginLowerCasePassword':'11221135d35eacd2de7b136d15be0662'} #ç»å½postæ°æ®        
        headers_sign = {"Host":"talent.woordee.com", "Connection":"keep-alive", "Content-Length":"0",
                   "Accept":"*/*", "Origin":"https://talent.woordee.com", "X-Requested-With":"XMLHttpRequest",
                   "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36",
                   "Content-Type":"application/x-www-form-urlencoded",
                   "Referer":"https://talent.woordee.com/square/center",
                   "Accept-Encoding":"gzip, deflate, br",
                   "Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8"
                  }
        sign_data = {'translatorId':'WE16104633TR'}       
    
        #get cookie
        kk = s.get('https://talent.woordee.com/users/login', headers=headers_resp).cookies.get_dict()
        #print (kk)
        kk_re = '\"Cookie\": ' + '\"SESSION=' + kk['SESSION'] + '\"'
        print (kk_re)
        
        #login
        log = s.post('https://talent.woordee.com/users/doLogin', data=login_data, headers=headers_login)
        print ("logged in")
        print (log)
        
        #get the sign count before sign
        s.post('https://talent.woordee.com/checkLogin', headers=headers_sign)
        countBf=s.post('https://talent.woordee.com/square/operate/signdetail', headers=headers_sign).json()
        #print (countBf)
        signBf=countBf['signInfo']['sign']
        print (signBf)
        
        #sign
        #s.post('https://talent.woordee.com/checkLogin', headers=headers_sign)
        #s.post('https://talent.woordee.com/square/operate/signdetail', headers=headers_sign)
        #s.post('https://talent.woordee.com/checkLogin', headers=headers_sign)
        s.post('https://talent.woordee.com/square/operate/sign', headers=headers_sign) #signing  
        print ("signing executed")
        
        #get the sign count after sign
        s.post('https://talent.woordee.com/checkLogin', headers=headers_sign)
        countAft=s.post('https://talent.woordee.com/square/operate/signdetail', headers=headers_sign).json()
        #print (countAft)
        result=countAft['signInfo']['sign']
        print (result)
        
        #judge the result
        if result:
            print ("congrats")
        else:
            global E
            E='result==False, signing failed'
            sendMail()
            
    except Exception as e:
        E=str(e)
        print (e)
        sendMail()

def sendMail():        
    print ("Failed in signing")
    msg = MIMEMultipart()
    body = MIMEText("ERROR happened from running sign.py, please check on Heroku immediately!\n\n" + "Detail:\n" + E)
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
