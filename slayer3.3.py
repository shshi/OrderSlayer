#-*- coding: utf-8 -*-
#===========================================================
# Author：Sha0hua
# E-mail:shi.sh@foxmail.com
# Modified Date: 2018-06-15
# Version: 3.3
# Version Description: added switch sate check
#===========================================================
from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.options import Options

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
sys.setrecursionlimit(1000000) #设置最大递归次数（若不设置，默认值为998，递归998次后将出现"maximum recursion depth exceeded"的报错）
 
def login():
    d.get('http://talent.woordee.com/front/truser.html')#WE登录页
    print "logging in..."
    #d.set_page_load_timeout(10)
    try:
        d.find_element_by_id("loginPhone").send_keys("18209347100") #输入手机号
        d.find_element_by_id("password").send_keys("ssh19198918") #输入密码
        d.find_element_by_xpath("//*[@onclick='login()']").click() #触发登录
        WebDriverWait(d, 20, 0.5).until(EC.presence_of_element_located((By.CLASS_NAME, 'myCode')))
    except:
        print "timeout"
    try:
        d.get("http://talent.woordee.com/front/task/taskCenter") #进入"订单中心"页面
        print "successfully logged in"
    except:
        print "successfully logged in (timeout)"

def switchOn():
    txt_off = "已关闭"
    state_bf = d.find_element_by_xpath('//*[@id="bs-example-navbar-collapse-1"]/ul[1]/li[1]/span').text
    if txt_off in state_bf:
        d.find_element_by_xpath('//*[@id="bs-example-navbar-collapse-1"]/ul[1]/li[1]/a/i').click()
        print "switch turned on"
    else:
        print "switch was on, no need to change"

def limit_YN():
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
        d.find_element_by_id(element)
        return True
    except:
        return False

def slay():
    d.set_page_load_timeout(10)
    try:
        print "game on"
        d.find_element_by_link_text("领取订单").click()
        print 'slayed'
        print '\a' #播放提示音
        time.sleep(7)
    except Exception as e:
        print e
        print '\a'
        slay()
        
def refreshPg():
    d.set_page_load_timeout(10)
    try:      
        #print "refresh"
        d.get("http://talent.woordee.com/front/task/taskCenter")
        WebDriverWait(d, 7, 0.5).until(EC.presence_of_element_located((By.CLASS_NAME, 'like')))
    except Exception as e:
        print e
        print '\a'
        time.sleep(5)
        d.get_screenshot_as_file('Error.png')
        print "continue hunting..."

def preView():
    d.set_page_load_timeout(1)
    try:
        d.find_element_by_xpath('//*[@id="mCSB_1_container"]/div/a').click() #点击“预览”
    except:
        pass
        
def hunt():
    try:
        if isElementExist("mCSB_1_container"): #判断是否存在“预览”，亦即判断是否有单           
            if d.find_element_by_xpath('//*[@id="mCSB_1_container"]/div/a').is_displayed(): #判断“预览”是否显示，亦即判断是否有新单          
                print 'new order found'
                preView()             
                if limitYes:
                    txt_word = d.find_element_by_xpath("//*[@class='words col-xs-12 col-md-2 nonePadding']").text[0:-3] #获取订单字数
                    num_word = float (txt_word) #转换订单字数为数值类型
                    print "%d words order"%num_word
                    if num_word <= limit:
                        slay()
                    else: 
                        print "over %d words. continue hunting..."%limit

                        #保存页面源码
                        #page = d.page_source
                        #log = open('aftPreview.html', 'w')
                        #log.write(page)
                        #log.close()
                            
                        refreshPg()
                        hunt()
                else: #若无字数限制
                    slay()
            else: #若“预览”不显示
                refreshPg()
                hunt()
        else: #若不存在“预览”
            refreshPg() #刷新页面
            hunt()
    except Exception as e:
        print e
        refreshPg()
        #time.sleep(3)
        print 'continue hunting...'
        hunt()

if __name__ == "__main__":
    firefoxProfile = FirefoxProfile()
    #firefoxProfile.set_preference('permissions.default.stylesheet', 2) #禁加载CSS
    firefoxProfile.set_preference('permissions.default.image', 2) #禁加载图片
    firefoxProfile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false') #禁加载Flash
    options = Options()
    options.add_argument('-headless') #无浏览器参数
    d=webdriver.Firefox(firefoxProfile, firefox_options=options)
    d.set_window_size(1600, 900)
    print "initiating..."        
    login()
    switchOn()
    limitYes = limit_YN()
    d.get_screenshot_as_file('HuntingGround.png')  # 保存网页截图
    #print "current title: %s"%d.title
    print "hunting..."
    hunt()
    print "the end"
    d.quit()
