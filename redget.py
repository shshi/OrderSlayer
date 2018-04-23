#-*- coding: utf-8 -*-
#===========================================================
# Name: redget
# Author：Sha0hua
# E-mail:shi.sh@foxmail.com
# Modified Date: 2018-04-23
# Version: 1.0
# Description: get red packet from talent.woordee.com
#===========================================================
from selenium import webdriver
import time
import logging
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def sign(b): 
    b.find_element_by_id("loginPhone").send_keys("18209347100") #输入手机号
    b.find_element_by_id("loginPassword").send_keys("ssh19198918") #输入密码
    b.find_element_by_xpath("//*[@onclick='login()']").click() #触发登录
    b.find_element_by_class_name("btn-sign").click()
    
#b=webdriver.PhantomJS('phantomjs')
#b.set_window_size(1600, 900)
b=webdriver.Firefox()
b.get("http://talent.woordee.com/front/truser") #WE登录页
sign(b)
for i in range(1500):
    print i
    b.find_element_by_xpath('//*[@id="timeAtag"]').click()
    #b.refresh()
    if i < 1499:
        print "looping"
    else:
        print "finished!"




