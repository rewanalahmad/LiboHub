import pytest
from django.contrib.auth.models import User
from pytest_factoryboy import register
from tests.factorys import UserFactoray, ProductFactoray, CategorayFactoray
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

register(UserFactoray)
register(ProductFactoray)
register(CategorayFactoray)



@pytest.fixture()
def user_1(db,user_factoray):
    user=user_factoray.create()
    return user


@pytest.fixture(scope='class')
def Chrome_driver_init(request):
    options=webdriver.ChromeOptions()
    #add custom option
    options.add_argument('--headless')
    options.add_argument('--disable-infobars')
    options.add_argument('--start-maximized')
    chrome_driver=webdriver.Chrome(options=options,service=Service(ChromeDriverManager().install()))
    request.cls.driver=chrome_driver
    yield
    chrome_driver.close()


@pytest.fixture(params=['chrome','firefox'],scope='class')
def driver_init(request):
    if request.param== 'chrome':
        options=webdriver.ChromeOptions()
        options.add_argument('--headless')
        web_driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
    if request.param=='firefox':
        options=webdriver.FirefoxOptions()
        options.add_argument('--headless')
        web_driver=webdriver.Firefox(options=options)
    request.cls.driver=web_driver
    yield
    web_driver.close()