import pytest
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.mark.usefixtures("Chrome_driver_init")
class TestBrowser(LiveServerTestCase):
    def test_login_admin(self):
        options=webdriver.ChromeOptions()
        options.add_argument('--headless')
        driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
        driver.get('http://127.0.0.1:8000/admin/login/?next=/admin/')
        assert 'Log in | Django site admin' in driver.title

@pytest.mark.usefixtures('driver_init')
class TestUrlChrom():
    def test_open_url(self,live_server):
        self.driver.get('http://127.0.0.1:8000/admin/login/?next=/admin/')
        assert 'Log in | Django site admin' in self.driver.title
