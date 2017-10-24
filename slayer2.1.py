#-*- coding: utf-8 -*-
#===========================================================
# Author：Sha0hua
# E-mail:shi.sh@foxmail.com
# Modified Date: 2017-10-20
# Version: 2.1
# Version Description: optimized hunting loop with new method
#===========================================================
from selenium import webdriver
import requests
import time
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
sys.setrecursionlimit(1000000) #设置最大递归次数（若不设置，默认值为998，递归998次后将出现"maximum recursion depth exceeded"的报错）
      
def login():
    print "logging in..."
    b.find_element_by_id("loginPhone").send_keys("18209347100") #输入手机号
    b.find_element_by_id("loginPassword").send_keys("ssh19198918") #输入密码
    b.find_element_by_xpath("//*[@onclick='login()']").click() #触发登录
    b.get("http://talent.woordee.com/front/task/taskCenter") #进入"订单中心"页面
    print "successfully logged in"

def YN():
    yn = raw_input('need a word limit?[Y/N] ')
    while yn != "Y" and yn != "N":
        print "wrong input, please input again(just type 'Y' or 'N') "
        yn = raw_input('need a word limit?[Y/N] ')
    if yn == "Y":
        global limit
        while True:
            try:
                limit = input('please input the limit: ')
                return True
            except:
                print "this is not a digit, please input again"
                continue
    else:
        return False

def isElementExist(element):
    try:
        b.find_element_by_id(element)
        return True
    except:
        return False

def slay():
    try:
        b.find_element_by_link_text("领取订单").click()
        print 'slayed'
        print '\a' #播放提示音
        time.sleep(7)
    except:
        print "preview time"
        slay()

def hunt():
    s = requests.session()
    log_data = {'loginPhone':'18209347100','loginPassword':'ssh19198918'} #登录post数据
    
    #登录操作
    log = s.post('http://talent.woordee.com/front/truser/login', log_data) #post登录地址
    s.get('http://talent.woordee.com/front/truser/userCenter')
    html = s.get('http://talent.woordee.com/front/task/taskCenter') #get登陆后的地址

    i = 'id="previewBtn'
    while not i in html.content:
        #print "no order"
        time.sleep(1)
        continue
    else:
        print "new order found"
        b.refresh()
        b.find_element_by_xpath('//*[@id="mCSB_1_container"]/div/a').click() #点击“预览”
        if YN:
            txt_word = b.find_element_by_xpath("//*[@class='words col-xs-12 col-md-2 nonePadding']").text[0:-3] #获取订单字数
            num_word = float (txt_word) #转换订单字数为数值类型
            print "%d words order"%num_word
            if num_word <= limit:
                slay()
            else: 
                print "over %d words, let it go\ncontinue hunting..."%limit
                time.sleep(3)
                hunt()
        else: #若无字数限制
            slay()

print "initiating..."
b=webdriver.PhantomJS('phantomjs') #无浏览器模式
b.implicitly_wait(7)
#b=webdriver.Firefox() #浏览器可视模式
#b.set_window_size(1600, 900)
#b.maximize_window()
b.get("http://talent.woordee.com/front/truser") #WE登录页       
login()
YN = YN()
print "hunting..."
hunt()
