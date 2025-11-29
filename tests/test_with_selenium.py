from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time


class Hosttest(LiveServerTestCase):
    def test_homepage(self):
        driver=webdriver.Chrome(service=Service(ChromeDriverManager().install())) #use when ever browser u use
        #driver.get(self.live_server_url)
        driver.get('http://127.0.0.1:8000/homepage/')

        #time.sleep(6)  #open default screen 5 secound befor close 
        assert 'LIBOHUB' in driver.title


class LoginFormTest(LiveServerTestCase):
		def testform(self):
			options = Options()
			options.headless = True
			driver = webdriver.Chrome(options=options)
			driver.get('http://127.0.0.1:8000/accounts/login/')
			user_name = driver.find_element('Username')
			user_password = driver.find_element('Password')
			submit = driver.find_element_by_id('submit')

			user_name.send_keys('rewan99')
			user_password.send_keys('47365585')

			submit.send_keys(Keys.RETURN)

			assert 'rewan99' in driver.page_source