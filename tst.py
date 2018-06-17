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
from requests_html import HTMLSession
import re

def sign():
    try:
        #登录及签到post数据准备
        session = HTMLSession()
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
        log = session.post('http://talent.woordee.com/front/truser/login', log_data) #post登录地址 
        r = session.get('http://talent.woordee.com/front/square') #get登陆后的地址
        
        print (r.content)
        print (r.html.render())
        
    except Exception as e:
        print (e)

sign()
