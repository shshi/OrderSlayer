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
        d.get('http://talent.woordee.com/front/circle/circleHome/b923cb623ffc411ca9939f8d012ef5ec')
    except:
        print "timeout"

def ShowMore():
    js = "document.getElementById('showMoreDiv').style.display='block'"
    d.execute_script(js)
    d.find_element_by_xpath('//*[@id="showMoreDiv"]/a').click()
    time.sleep(3)

def Harvest():
    print "checking..."
    list_get = d.find_elements_by_link_text("领红包>")
    #print list_get
    if list_get:
        n=0
        for i in list_get:
            i.click()
            d.find_element_by_xpath('/html/body/div[5]/div/a[1]').click()
            txt = d.find_element_by_xpath('/html/body/div[6]/div/div/p').text
            if "恭喜" in txt:
                n+=1
                print "No.%d"%n
                d.find_element_by_xpath('/html/body/div[6]/div/a').click() #关闭红包窗口
                continue
            else:
                print "exprired left"
                break              
        while n == 15:
            print "more content"
            ShowMore()
            Harvest()
    else:
        print "No new red package"   
        
if __name__ == "__main__":
    firefoxProfile = FirefoxProfile()
    #firefoxProfile.set_preference('permissions.default.stylesheet', 2) #禁加载CSS
    firefoxProfile.set_preference('permissions.default.image', 2) #禁加载图片
    firefoxProfile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false') #禁加载Flash
    options = Options()
    #options.add_argument('-headless') #无浏览器参数
    d=webdriver.Firefox(firefoxProfile, firefox_options=options)
    d.set_window_size(1600, 900)
    print "initiating..."        
    login()
    Harvest()
    print "the end"
    #d.quit()
