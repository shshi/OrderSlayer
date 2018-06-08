#-*- coding: utf-8 -*-
#===========================================================
# Author：Sha0hua
# E-mail:shi.sh@foxmail.com
# Modified Date: 2018-06-07
# Version: 3.1
# Version Description: optimized refresh speed 
#===========================================================
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
sys.setrecursionlimit(1000000) #设置最大递归次数（若不设置，默认值为998，递归998次后将出现"maximum recursion depth exceeded"的报错）
 
def login():
    b.get('http://talent.woordee.com/front/truser.html')#WE登录页
    print "logging in..."
    #b.set_page_load_timeout(7)
    try:
        b.find_element_by_id("loginPhone").send_keys("18209347100") #输入手机号
        b.find_element_by_id("password").send_keys("ssh19198918") #输入密码
        b.find_element_by_xpath("//*[@onclick='login()']").click() #触发登录
        WebDriverWait(b, 9223372036854775807, 0.5).until(EC.presence_of_element_located((By.CLASS_NAME, 'myCode')))
        #b.get_screenshot_as_file('main.png')
    except:
        print "timeout"
    try:
        b.get("http://talent.woordee.com/front/task/taskCenter") #进入"订单中心"页面
        print "successfully logged in"
    except:
        print "successfully logged in (timeout)"    

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
        b.find_element_by_id(element)
        return True
    except:
        return False

def slay():
    b.set_page_load_timeout(180)
    try:
        print "Game On"
        b.find_element_by_link_text("领取订单").click()
        print 'slayed'
        print '\a' #播放提示音
        time.sleep(7)
    except:
        print "preview time"
        slay()
        
def refreshPg():
    try:
        b.set_page_load_timeout(10)
        #print "refresh"
        b.get("http://talent.woordee.com/front/task/taskCenter")
        #WebDriverWait(b, 7, 0.5).until(EC.presence_of_element_located((By.CLASS_NAME, 'like')))
    except Exception as e:
        print e
        b.refresh()
        time.sleep(3)
        print "continue hunting..."

def preView():
    b.set_page_load_timeout(1)
    try:
        b.find_element_by_xpath('//*[@id="mCSB_1_container"]/div/a').click() #点击“预览”
    except:
        pass
        
def hunt():
    try:
        if isElementExist("mCSB_1_container"): #判断是否存在“预览”，亦即判断是否有单           
            if b.find_element_by_xpath('//*[@id="mCSB_1_container"]/div/a').is_displayed(): #判断“预览”是否显示，亦即判断是否有新单          
                print 'new order found'
                preView()             
                if limitYes:
                    txt_word = b.find_element_by_xpath("//*[@class='words col-xs-12 col-md-2 nonePadding']").text[0:-3] #获取订单字数
                    num_word = float (txt_word) #转换订单字数为数值类型
                    print "%d words order"%num_word
                    if num_word <= limit:
                        slay()
                    else: 
                        print "over %d words. continue hunting..."%limit

                        #保存页面源码
                        #page = b.page_source
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
    dcap = dict(DesiredCapabilities.PHANTOMJS)
    dcap["phantomjs.page.settings.loadImages"] = False  # 禁止加载图片
    b=webdriver.PhantomJS(desired_capabilities=dcap) #无浏览器模式
    #b=webdriver.Firefox()
    b.set_window_size(1600, 900)
    print "initiating..."        
    login()
    limitYes = limit_YN()
    b.get_screenshot_as_file('OrderCenter.png')  # 保存网页截图
    #print "current title: %s"%b.title
    print "hunting..."
    hunt()
    print "finished"
    b.quit()
