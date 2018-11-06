# -*- coding:utf-8 -*-
#===========================================================
# Author：Sha0hua
# E-mail:shi.sh@foxmail.com
# Created Date: 2017-09-07
# Modified Date: 2018-06-20
# Version: 3.0
# Description: sign at Woordee website  
#===========================================================
import requests
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
                   "Cookie": "SESSION=6fdb29a3-8943-42af-b7dc-61c3d5b14558"
                  }
        login_data = {'loginPhone':'18209347100','loginPassword':'11221135d35eacd2de7b136d15be0662','loginLowerCasePassword':'11221135d35eacd2de7b136d15be0662'} #登录post数据        
        headers_sign = {"Host":"talent.woordee.com", "Connection":"keep-alive", "Content-Length":"25",
                   "Accept":"*/*", "Origin":"http://talent.woordee.com", "X-Requested-With":"XMLHttpRequest",
                   "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36",
                   "Content-Type":"application/x-www-form-urlencoded",
                   "Referer":"http://talent.woordee.com/front/square",
                   "Accept-Encoding":"gzip, deflate",
                   "Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8",
                   "Cookie": "_uab_collina=154139283253526626410393; SESSION=6fdb29a3-8943-42af-b7dc-61c3d5b14558"
                  }
        sign_data = {'translatorId':'WE16104633TR'} #签到post数据        
        headers_square = {"Host":"talent.woordee.com", "Connection":"keep-alive", "Upgrade-Insecure-Requests":"1",
                   "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36",
                    #"X-Requested-With": "XMLHttpRequest",
                   "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                   "Referer":"http://talent.woordee.com/front/truser/userCenter",
                   "Accept-Encoding":"gzip, deflate",
                   "Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8",
                   "Cookie": "_uab_collina=154139283253526626410393; SESSION=6fdb29a3-8943-42af-b7dc-61c3d5b14558"
                  }
    
        #登录操作
        log = s.post('https://talent.woordee.com/users/login', data=login_data, headers=headers_login) #post登录地址
        
        #签到前数据获取
        print ("logged in")
        
        #签到操作
        s.post('https://talent.woordee.com/square/operate/sign', headers=headers_sign) #触发签到  
        print ("Yes!")

        #签到后数据获取
    
sign()
