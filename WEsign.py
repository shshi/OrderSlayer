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
import re
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def sign():

    #登录及签到post数据准备
    s = requests.session()
    log_data = {'loginPhone':'18209347100','loginPassword':'ssh19198918'} #登录post数据
    sgn_data = {'translatorId':'WE16104633TR'} #签到post数据
    
    #登录操作
    log = s.post('http://talent.woordee.com/front/truser/login', log_data) #post登录地址 
    html = s.get('http://talent.woordee.com/front/truser/userCenter') #get登陆后的地址
    page = html.content
    #print page

    #签到操作
    s.post('http://talent.woordee.com/front/truser/sign', sgn_data)

    #提取签到结果并打印
    soup = BeautifulSoup(page,"html.parser")
    txt1 = soup.find_all('a', attrs={"class":"btn-sign"})[0].get_text() #提取"已签到"文本
    txt2 = soup.find_all('p', attrs={"class":"p2"})[0].get_text() #提取"连续签到n天"文本
    print txt1, txt2

sign()
time.sleep(3)