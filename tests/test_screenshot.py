import os
import time
import pytest
from selenium import webdriver
from django.test import LiveServerTestCase
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


def take_screenshot(driver,name):
    time.sleep(1)
    os.makedirs(os.path.join('screenshot',os.path.dirname(name)),exist_ok=True)
    driver.save_screenshot(os.path.join('screenshot',name))

def test_example(live_server):
    options=webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
    driver.get('http://127.0.0.1:8000/homepage/')
    take_screenshot(driver,'homepage.png')

