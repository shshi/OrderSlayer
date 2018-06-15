#-*- coding: utf-8 -*-
#===========================================================
# Author：Sha0hua
# E-mail:shi.sh@foxmail.com
# Modified Date: 2018-06-14
# Version: 1.0
# Description: get red packet from talent.woordee.com
#===========================================================
from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.options import Options
import time
import logging
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
sys.setrecursionlimit(1000000000)

def sign():
    d.get("http://talent.woordee.com/front/truser.html")
    print "logging in..."
    #d.set_page_load_timeout(10)
    d.find_element_by_id("loginPhone").send_keys("18209347100") #输入手机号
    d.find_element_by_id("password").send_keys("ssh19198918") #输入密码
    d.find_element_by_xpath("//*[@onclick='login()']").click() #触发登录
    print "successfully logged in"
       
def getRed():
    d.set_page_load_timeout(10)
    try:
        d.get("http://talent.woordee.com/front/square.html")
        time.sleep(3)
        txt_bf = d.find_element_by_id("transAmount").text[1:-2]
        #print "txt: %s"%txt
        amt_bf = float (txt_bf)
    except Exception as e:
        print e
        getRed()
    while amt_bf < 180000:
        try:
            d.get("http://talent.woordee.com/front/square.html")
            time.sleep(3)
            txt_aft = d.find_element_by_id("transAmount").text[1:-2]
            amt_aft = float (txt_aft)
        except Exception as e:
            print e
            print '\a'
            print "continue listening..."
            getRed()
        if amt_bf == amt_aft:
            getRed()
        elif amt_aft >= 180000:       
            print '\a'
            break
        else:
            print "%d"%amt_aft
            print '\a'
            getRed()
    print "now!"
    print '\a'
    d.find_elements_by_link_text('抢')[1].click()
    d.find_elements_by_link_text('抢')[5].click()
    #d.find_elements_by_class_name('redGet')[5].click()
    #driver.find_element_by_css_selector("[type=submit]").click()
    print "done"

if __name__ == "__main__":
    firefoxProfile = FirefoxProfile()
    #firefoxProfile.set_preference('permissions.default.stylesheet', 2) #禁加载CSS
    firefoxProfile.set_preference('permissions.default.image', 2) #禁加载图片
    firefoxProfile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false') #禁加载Flash
    options = Options()
    options.add_argument('-headless') #无浏览器参数
    d=webdriver.Firefox(firefoxProfile, firefox_options=options)
    d.set_window_size(1600, 900)
    sign()
    print "listening..."
    getRed()
