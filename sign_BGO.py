#-*- coding: utf-8 -*-
#===========================================================
# Name: WE_autosign
# Author：Sha0hua
# E-mail:shi.sh@foxmail.com
# Modified Date: 2017-09-01
# Version: 1.0
#===========================================================
from selenium import webdriver
import time
import logging
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

b=webdriver.PhantomJS('phantomjs') #无浏览器模式
#b=webdriver.Firefox() #浏览器可视模式
b.set_window_size(1600, 900)
b.get("http://talent.woordee.com/front/truser") #WE登录页

def sign(b):
    #print "正在登录..."
    b.find_element_by_id("loginPhone").send_keys("18209347100") #输入手机号
    b.find_element_by_id("loginPassword").send_keys("ssh19198918") #输入密码
    b.find_element_by_xpath("//*[@onclick='login()']").click() #触发登录
    #print "正在签到..."
    b.find_element_by_xpath("//*[@class='btn-sign']").click() #触发签到
    #print b.current_url
    s = b.find_elements("css selector", ".btn-sign") #获取签到状态
    c = b.find_element_by_class_name("p2") #获取连续签到天数
    log = '%s, %s!'%(s[0].text, c.text) #日志内容
    print log
    
    #日志文件的建立
    logging.basicConfig(level=logging.DEBUG,  
                        format='%(asctime)s %(levelname)s %(message)s',  
                        datefmt='%a, %d %b %Y %H:%M:%S',  
                        filename='./WE_log.log',  
                        filemode='a')    
    logging.info(log)

sign(b)
