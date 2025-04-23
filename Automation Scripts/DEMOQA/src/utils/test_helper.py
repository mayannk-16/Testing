import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from ..config.config import TestConfig

class TestHelper:
    @staticmethod
    def get_driver():
        options = webdriver.ChromeOptions()
        if TestConfig.HEADLESS:
            options.add_argument('--headless')
        
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        driver.implicitly_wait(TestConfig.IMPLICIT_WAIT)
        return driver

    @staticmethod
    def api_request(method, endpoint, **kwargs):
        import requests
        url = f"{TestConfig.API_BASE_URL}{endpoint}"
        return requests.request(method, url, **kwargs)