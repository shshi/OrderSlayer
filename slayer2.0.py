#-*- coding: utf-8 -*-
#===========================================================
# Author：Sha0hua
# E-mail:shi.sh@foxmail.com
# Modified Date: 2017-09-27
# Version: 2.0
# Version Description: added order word limit 
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
    print "successfully logged in"
    #page = b.page_source.encode('gbk', 'ignore') #获取页面源码
    #print page

def isElementExist(element):
    try:
        b.find_element_by_id(element)
        return True
    except:
        return False

def hunt():
    print "hunting..."
    try:
        if isElementExist("mCSB_1_container"): #判断是否存在“预览”，亦即判断是否有单           
            if b.find_element_by_xpath('//*[@id="mCSB_1_container"]/div/a').is_displayed(): #判断“预览”是否显示，亦即判断是否有新单          
                print 'new order found'
                txt_word = b.find_element_by_xpath("//*[@class='words col-xs-12 col-md-2 nonePadding']").text[0:-3] #获取订单字数
                num_word = float (txt_word) #转换订单字数为数值类型
                if num_word <= limit:
                    print "%s words order"%txt_word
                    #print b.find_element_by_xpath("//*[@class='words col-xs-12 col-md-2 nonePadding']").text
                    b.find_element_by_xpath('//*[@id="mCSB_1_container"]/div/a').click() #点击“预览”
                    #b.find_element_by_link_text("预览")[0].click() #点击“预览”
                    #b.find_element_by_xpath("//*[@class='btnNoBg btn btn-link']").click() #点击“预览”

                    #保存页面源码
                    #page = b.page_source.encode('gbk', 'ignore')
                    #log = open('page.log', 'a')
                    #log.write(page)
                    #log.close()
            
                    b.find_element_by_link_text("领取订单").click() #点击“领取订单”
                    print 'slayed'
                    print '\a' #播放提示音
                    #os.popen('Taste.mp3') #播放本地音乐文件
                    #os.system('start Taste.mp3')
                    time.sleep(7)
                else:
                    print "over %d words, let it go"%limit
                    b.refresh()
                    hunt()
            else:
                b.refresh()
                hunt()
        else:
            #print 'no order'
            b.refresh() #刷新页面
            #b.find_element_by_xpath("//*[@class='refresh col-md-2']").click()#点击“刷新订单”
            hunt()
    except Exception as e:
        print e
        b.refresh()
        time.sleep(3)
        print 'continue hunting...'
        hunt()   

login()
limit = input('please input word limit:') #输入接单字数限制
hunt()
