import os
import time
import pytest
from selenium import webdriver

def take_screenshot(driver,name):
    time.sleep(1)
    os.makedirs(os.path.join('screenshot',os.path.dirname(name)),exist_ok=True)
    driver.save_screenshot(os.path.join('screenshot',name))