#-*- coding: utf-8 -*-
#===========================================================
# Author：Sha0hua
# E-mail:shi.sh@foxmail.com
# Modified Date: 2017-09-26
# Version: 1.0
#===========================================================
from selenium import webdriver
import time
import os
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

sys.setrecursionlimit(100000) #设置最大递归次数（若不设置，默认值为998，递归998次后将出现"maximum recursion depth exceeded"的报错）

b=webdriver.PhantomJS('phantomjs')
b.set_window_size(1600, 900)
b.get("http://talent.woordee.com/front/truser") #WE登录页

def login():
    print "logging in..."
    b.find_element_by_id("loginPhone").send_keys("18209347100") #输入手机号
    b.find_element_by_id("loginPassword").send_keys("ssh19198918") #输入密码
    b.find_element_by_xpath("//*[@onclick='login()']").click() #触发登录
    b.get("http://talent.woordee.com/front/task/taskCenter") #进入"订单中心"页面
    print "successfully logged in\nhunting..."

def isElementExist(element):
    try:
        b.find_element_by_id(element)
        return True
    except:
        return False

def hunt():
    try:
        if isElementExist("mCSB_1_container"): #判断是否存在“预览”，亦即判断是否有单
            if b.find_element_by_xpath('//*[@id="mCSB_1_container"]/div/a').is_displayed(): #判断“预览”是否显示，亦即判断是否有新单          
                print 'new order found'
                b.find_element_by_xpath('//*[@id="mCSB_1_container"]/div/a').click() #点击“预览”          
                b.find_element_by_link_text("领取订单").click() #点击“领取订单”
                print 'slayed'
                print '\a' #播放提示音
                time.sleep(7)
            else:
                b.refresh()
                hunt()
        else:
            b.refresh() #刷新页面
            hunt()
    except Exception as e:
        print e
        b.refresh()
        time.sleep(3)
        print 'continue hunting...'
        hunt()   

login()
hunt()
