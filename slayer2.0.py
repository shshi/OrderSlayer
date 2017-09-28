#-*- coding: utf-8 -*-
#===========================================================
# Author：Sha0hua
# E-mail:shi.sh@foxmail.com
# Modified Date: 2017-09-27
# Version: 2.0
# Version Description: added choice of order word limit 
#===========================================================
from selenium import webdriver
import time
import os
import sys

def login():
    print "logging in..."
    b.find_element_by_id("loginPhone").send_keys("18209347100") #输入手机号
    b.find_element_by_id("loginPassword").send_keys("ssh19198918") #输入密码
    b.find_element_by_xpath("//*[@onclick='login()']").click() #触发登录
    b.get("http://talent.woordee.com/front/task/taskCenter") #进入"订单中心"页面
    print "successfully logged in"


def YN():
    yn = raw_input('need to set a word limit?[Y/N] ')
    if yn != "Y" and yn != "N":
        print "wrong input, please input again(just type 'Y' or 'N') "
        YN()
    elif yn == "Y":
        global limit
        limit = input('please input word limit: ') #输入接单字数限制       
        return True
    else:
        return False

def isElementExist(element):
    try:
        b.find_element_by_id(element)
        return True
    except:
        return False

def slay():
    b.find_element_by_xpath('//*[@id="mCSB_1_container"]/div/a').click() #点击“预览”           
    b.find_element_by_link_text("领取订单").click() #点击“领取订单”
    print 'slayed'
    print '\a' #播放提示音
    time.sleep(7)

def hunt():
    try:
        if isElementExist("mCSB_1_container"): #判断是否存在“预览”，亦即判断是否有单           
            if b.find_element_by_xpath('//*[@id="mCSB_1_container"]/div/a').is_displayed(): #判断“预览”是否显示，亦即判断是否有新单          
                print 'new order found'
                if YN():
                    txt_word = b.find_element_by_xpath("//*[@class='words col-xs-12 col-md-2 nonePadding']").text[0:-3] #获取订单字数
                    num_word = float (txt_word) #转换订单字数为数值类型
                    if num_word <= limit:
                        print "%s words order"%txt_word
                        slay()
                    else:
                        print "over %d words, let it go"%limit
                        b.refresh()
                        hunt()
                else:
                    slay()
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

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    sys.setrecursionlimit(100000) #设置最大递归次数（若不设置，默认值为998，递归998次后将出现"maximum recursion depth exceeded"的报错）
    b=webdriver.PhantomJS('phantomjs')
    b.set_window_size(1600, 900)
    b.get("http://talent.woordee.com/front/truser") #WE登录页
    login()
    YN()
    print "hunting..."
    hunt()
