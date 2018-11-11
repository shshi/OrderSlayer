#-*- coding: utf-8 -*-
#===========================================================
# Author：Sha0hua
# E-mail:shi.sh@foxmail.com
# Modified Date: 2018-06-15
# Version: 3.3
# Version Description: added switch sate check
#===========================================================
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
                   "Cookie": "_uab_collina=154139283253526626410393; SESSION=6fdb29a3-8943-42af-b7dc-61c3d5b14558"
                  }
        login_data = {'loginPhone':'18209347100','loginPassword':'11221135d35eacd2de7b136d15be0662','loginLowerCasePassword':'11221135d35eacd2de7b136d15be0662'} #ç»å½postæ°æ®        
        headers_sign = {"Host":"talent.woordee.com", "Connection":"keep-alive", "Content-Length":"0",
                   "Accept":"*/*", "Origin":"https://talent.woordee.com", "X-Requested-With":"XMLHttpRequest",
                   "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36",
                   "Content-Type":"application/x-www-form-urlencoded",
                   "Referer":"https://talent.woordee.com/square/center",
                   "Accept-Encoding":"gzip, deflate",
                   "Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8",
                   "Cookie": "SESSION=6fdb29a3-8943-42af-b7dc-61c3d5b14558"
                  }
        sign_data = {'translatorId':'WE16104633TR'}       
        headers_square = {"Host":"talent.woordee.com", "Connection":"keep-alive", "Upgrade-Insecure-Requests":"1",
                   "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36",
                    #"X-Requested-With": "XMLHttpRequest",
                   "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                   "Referer":"http://talent.woordee.com/front/truser/userCenter",
                   "Accept-Encoding":"gzip, deflate",
                   "Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8",
                   "Cookie": "_uab_collina=154139283253526626410393; SESSION=6fdb29a3-8943-42af-b7dc-61c3d5b14558"
                  }
    
        #ç»å½æä½
        log = s.post('https://talent.woordee.com/users/doLogin', data=login_data, headers=headers_login) #
        
        #ç­¾å°åæ°æ®è·å
        print ("logged in")
        
        #ç­¾å°æä½
        s.post('https://talent.woordee.com/square/operate/sign', headers=headers_sign) #è§¦åç­¾å°  
        print ("Yes!")
