#-*- coding: utf-8 -*-
#===========================================================
# Name: redget
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
    d.get("http://talent.woordee.com/front/square.html")
    while d.find_element_by_xpath('/html/body/div[2]/div[1]/ul/li[1]/div[2]/p[1]').is_displayed():
        print "not yet"
    print "now!"
    d.find_element_by_xpath('//*[@id="timeAtag"]').click()
    d.find_element_by_xpath('/html/body/div[2]/div[1]/ul/li[2]/div[1]/a').click()   
    print "done"

if __name__ == "__main__":
    firefoxProfile = FirefoxProfile()
    #firefoxProfile.set_preference('permissions.default.stylesheet', 2) #禁加载CSS
    firefoxProfile.set_preference('permissions.default.image', 2) #禁加载图片
    firefoxProfile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false') #禁加载Flash
    options = Options()
    #options.add_argument('-headless') #无浏览器参数
    d=webdriver.Firefox(firefoxProfile, firefox_options=options)
    d.set_window_size(1600, 900)
    sign()
    getRed()
