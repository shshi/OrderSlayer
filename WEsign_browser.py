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

def sign(b): 
    b.find_element_by_id("loginPhone").send_keys("18209347100") #输入手机号
    b.find_element_by_id("loginPassword").send_keys("ssh19198918") #输入密码
    b.find_element_by_xpath("//*[@onclick='login()']").click() #触发登录
    b.find_element_by_xpath("//*[@class='btn-sign']").click() #触发签到

b=webdriver.Firefox()
b.get("http://talent.woordee.com/front/truser") #WE登录页
sign(b)

# define the log file, file mode and logging level
logging.basicConfig(level=logging.DEBUG,  
                    format='%(asctime)s %(levelname)s %(message)s',  
                    datefmt='%a, %d %b %Y %H:%M:%S',  
                    filename='./WE_log.log',  
                    filemode='a')
logging.info('Successfully signed!')
print "Successfully signed!"
