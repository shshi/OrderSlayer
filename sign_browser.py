#-*- coding: utf-8 -*-
#===========================================================
# Name: WE_autosign
# Author：Sha0hua
# E-mail:shi.sh@foxmail.com
# Modified Date: 2018-06-14
# Version: 1.0
#===========================================================
from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.options import Options
import time
import logging
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def sign():
    d.get("http://talent.woordee.com/front/truser") 
    d.find_element_by_id("loginPhone").send_keys("18209347100") 
    d.find_element_by_id("password").send_keys("ssh19198918") 
    d.find_element_by_xpath("//*[@onclick='login()']").click() 
    print "successfully logged in"
    d.get("http://talent.woordee.com/front/square.html")
    d.find_element_by_xpath('//*[@id="ySign"]').click()
    if d.find_element_by_id("nSign").is_displayed():
        print "sign failed"
        while True:
            print '\a'
            time.sleep(1)
    else:
        print "successfully signed"
        # define the log file, file mode and logging level
        logging.basicConfig(level=logging.DEBUG,  
                            format='%(asctime)s %(levelname)s %(message)s',  
                            datefmt='%a, %d %b %Y %H:%M:%S',  
                            filename='./WE_log.log',  
                            filemode='a')
        logging.info('Successfully signed!')

if __name__ == "__main__":
    firefoxProfile = FirefoxProfile()
    firefoxProfile.set_preference('permissions.default.image', 2)
    firefoxProfile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')
    options = Options()
    options.add_argument('-headless')
    d=webdriver.Firefox(firefoxProfile, firefox_options=options)
    d.set_window_size(1600, 900)
    sign()
    time.sleep(7)
    d.quit()


