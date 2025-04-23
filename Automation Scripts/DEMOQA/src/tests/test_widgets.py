import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.pages.widgets_page import WidgetsPage
from src.utils.test_helper import TestHelper
from src.config.config import TestConfig

@allure.epic("DemoQA Testing")
@allure.feature("Widgets Testing")
class TestWidgets:
    @pytest.fixture
    def driver(self):
        driver = TestHelper.get_driver()
        driver.maximize_window()
        driver.implicitly_wait(20)
        yield driver
        driver.quit()

    @pytest.fixture
    def widgets_page(self, driver):
        return WidgetsPage(driver)

    @allure.story("Accordion Testing")
    def test_accordion(self, driver, widgets_page):
        with allure.step("Navigate to Accordion"):
            driver.get(TestConfig.BASE_URL + "/accordion")
            
        with allure.step("Test accordion sections"):
            widgets_page.click_accordion_section(1)
            assert widgets_page.is_accordion_content_visible(1)
            
            widgets_page.click_accordion_section(2)
            assert widgets_page.is_accordion_content_visible(2)

    @allure.story("Date Picker Testing")
    def test_date_picker(self, driver, widgets_page):
        with allure.step("Navigate to Date Picker"):
            driver.get(TestConfig.BASE_URL + "/date-picker")
            
        with allure.step("Set and verify date"):
            test_date = "03/15/2024"
            widgets_page.set_date(test_date)
            assert widgets_page.get_date() == test_date