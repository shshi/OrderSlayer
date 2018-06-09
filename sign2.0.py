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

        #签到前数据获取
        page0 = s.get('http://talent.woordee.com/front/square').content
        #reg = r"<a href='(.*?)'>The Beijing Hour"
        reg = r'<em class="signedCount">(.*?)天</em>'
        num_re = re.compile(reg)
        A=re.findall(num_re,page0)
        print (A)
        print ("AAAAA")
        soup = BeautifulSoup(page0,"html.parser")
        try:
            #txt_bf = soup.find_all('em', attrs={"class":"signedCount"})[0].get_text()
            txt_bf = soup.find_all('em', attrs={"class":"signedCount"}).string
            #num_bf = re.findall(r"\d+", txt_bf)
            print (txt_bf)
        except Exception as e:
            print (e)
    except:
        print ("error")

sign()
