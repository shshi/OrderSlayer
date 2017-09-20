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
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

b=webdriver.PhantomJS('phantomjs')
b.set_window_size(1600, 900)
b.get("http://talent.woordee.com/front/truser") #WE登录页

def login(b):
    #print "正在登录..."
    b.find_element_by_id("loginPhone").send_keys("18209347100") #输入手机号
    b.find_element_by_id("loginPassword").send_keys("ssh19198918") #输入密码
    b.find_element_by_xpath("//*[@onclick='login()']").click() #触发登录
    b.get("http://talent.woordee.com/front/task/taskCenter")
    #page = b.page_source.encode('gbk', 'ignore')
    #print page
    
def hunt(b):
    try:
        if b.find_element_by_xpath("//*[@class='btnNoBg btn btn-link']").is_displayed(): #判断“预览”是否显示，亦即判断是否有单
            print 'new order!'
            b.find_element_by_xpath("//*[@class='btnNoBg btn btn-link']").click() #点击“预览”
            b.find_element_by_link_text("领取订单").click() #点击“领取订单”
            print 'slayed'
            time.sleep(7)
        else:
            print 'no order'
            b.refresh #刷新页面
            #b.find_element_by_xpath("//*[@class='refresh col-md-2']").click()#点击“刷新订单”
            hunt(b)
    except:
        b.refresh
        time.sleep(2)
        hunt(b)   

login(b)
hunt(b)
