#-*- coding: utf-8 -*-
#===========================================================
# Author：Sha0hua
# E-mail:shi.sh@foxmail.com
# Modified Date: 2018-09-19
# Version: 2.1
#===========================================================
from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.options import Options

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
sys.setrecursionlimit(1000000) #设置最大递归次数（若不设置，默认值为998，递归998次后将出现"maximum recursion depth exceeded"的报错）

class Main():
    Sum=0
    
    def login(self):
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

    def ShowMore(self):
        js = "document.getElementById('showMoreDiv').style.display='block'"
        d.execute_script(js)
        d.find_element_by_xpath('//*[@id="showMoreDiv"]/a').click()
        time.sleep(3)

    def Loop(self):
        print "checking..."
        global n
        n=0
        list_get = d.find_elements_by_link_text("领红包>")
        #print len(list_get)
        if list_get:
            for i in list_get:
                i.click()
                d.find_element_by_xpath('/html/body/div[5]/div/a[1]').click() #点击打开红包
                txt = d.find_element_by_xpath('/html/body/div[6]/div/div/p').text #获取窗口文字文本
                if "恭喜" in txt:
                    n+=1
                    amt_str=str(d.find_element_by_xpath('/html/body/div[6]/div/span[2]').text) #获取红包金额
                    amt_num=filter(lambda ch: ch in '0123456789.', amt_str)
                    amt_num=float(amt_num)
                    print "No.%d. %f"%(n, amt_num)
                    self.Sum+=amt_num
                    d.find_element_by_xpath('/html/body/div[6]/div/a').click() #关闭红包窗口
                    continue
                else:
                    print "exprired left"
                    break        
        else:
            print "No new red package"   
    def Harvest(self):
        rop=0
        self.Loop()
        while n == 15:
            print "more content"
            rop+=1
            d.refresh()
            for x in range(rop):
                self.ShowMore()
            self.Loop()
        print "sum: %f"%self.Sum

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
    H=Main()
    H.login()
    H.Harvest()
    print "the end"
    time.sleep(12)
    d.quit()
