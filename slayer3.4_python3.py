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
#reload(sys)
#sys.setdefaultencoding('utf-8')
sys.setrecursionlimit(1000000) #设置最大递归次数（若不设置，默认值为998，递归998次后将出现"maximum recursion depth exceeded"的报错）
 
def login():
    d.get('https://talent.woordee.com/')
    d.find_element_by_class_name("login-btn").click()
    d.get('https://talent.woordee.com/users/login')#WE登录页
    time.sleep(10)
    print ("logging in...")
    try:
        d.find_element_by_class_name("tel").send_keys("18869876502") #输入手机号
        d.find_element_by_id("password").send_keys("s.1") #输入密码
        #d.find_element_by_class_name("green-btn submit-btn").click() #触发登录
        d.find_element_by_xpath("/html/body/div[2]/div/div[2]/form/input").click()
        #WebDriverWait(d, 20, 0.5).until(EC.presence_of_element_located((By.CLASS_NAME, 'myCode')))
    except Exception as e:
        print (e)
        print ("timeout")
    try:
        d.get("https://talent.woordee.com/task/center") #进入"订单中心"页面
        print ("successfully logged in")
    except:
        print ("successfully logged in (timeout)")

def switchOn():
    txt_off = "已关闭"
    state_bf = d.find_element_by_xpath('//*[@id="bs-example-navbar-collapse-1"]/ul[1]/li[1]/span').text
    if txt_off in state_bf:
        d.find_element_by_xpath('//*[@id="bs-example-navbar-collapse-1"]/ul[1]/li[1]/a/i').click()
        print ("switch turned on")
    else:
        print ("switch was on, no need to change")

def limit_YN():
    yn = input('need a word limit?[Y/N] ')
    while yn != "Y" and yn != "N":
        print ("wrong input, please input again(just type 'Y' or 'N') ")
        yn = input('need a word limit?[Y/N] ')
    if yn == "Y":
        global limit
        while True:
            try:
                limit = input('please input the limit: ')
                return True
            except:
                print ("this is not a digit, please input again")
                continue
    else:
        return False

def isElementExist(element):
    try:
        d.find_element_by_class_name(element)
        return True
    except:
        return False

def slay():
    d.set_page_load_timeout(10)
    try:
        print ("game on")
        d.find_element_by_link_text("领取").click()
        print ('slayed')
        print ('\a') #播放提示音
        time.sleep(7)
    except Exception as e:
        print (e)
        print ('\a')
        slay()
        
def refreshPg():
    d.set_page_load_timeout(10)
    try:      
        #print "refresh"
        d.get("https://talent.woordee.com/task/center")
        #WebDriverWait(d, 7, 0.5).until(EC.presence_of_element_located((By.CLASS_NAME, 'like')))
    except Exception as e:
        print (e)
        print ('\a')
        time.sleep(5)
        d.get_screenshot_as_file('Error.png')
        print ("continue hunting...")

def preView():
    d.set_page_load_timeout(1)
    try:
        d.find_element_by_class_name('preview-btn').click() #点击“预览”
    except:
        pass
        
def hunt():
    try:
        if isElementExist("preview-btn"): #判断是否存在“预览”，亦即判断是否有单              
            print ('new order found')
            preView()             
            if limitYes:
                txt_word = d.find_element_by_class_name("order-word").text[0:-1] #获取订单字数
                num_word = float (txt_word) #转换订单字数为数值类型
                print ("%d words order"%num_word)
                if num_word <= limit:
                    slay()
                else: 
                    print ("over %d words. continue hunting..."%limit)
                    refreshPg()
                    hunt()
            else: #若无字数限制
                slay()
        else: #若不存在“预览”
            refreshPg() #刷新页面
            hunt()
    except Exception as e:
        print (e)
        refreshPg()
        #time.sleep(3)
        print ('continue hunting...')
        hunt()

if __name__ == "__main__":
    firefoxProfile = FirefoxProfile()
    #firefoxProfile.set_preference('permissions.default.stylesheet', 2) #禁加载CSS
    firefoxProfile.set_preference('permissions.default.image', 2) #禁加载图片
    firefoxProfile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false') #禁加载Flash
    firefoxProfile.accept_untrusted_certs = True
    options = Options()
    options.add_argument('-headless') #无浏览器参数
    d=webdriver.Firefox(firefoxProfile, options=options)
    d.set_window_size(1600, 900)
    print ("initiating..." )       
    login()
    #switchOn()
    limitYes = limit_YN()
    d.get_screenshot_as_file('HuntingGround.png')  # 保存网页截图
    #print "current title: %s"%d.title
    print ("hunting...")
    hunt()
    print ("the end")
    d.quit()
