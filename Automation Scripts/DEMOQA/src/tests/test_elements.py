import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.pages.elements_page import ElementsPage
from src.utils.test_helper import TestHelper
from src.config.config import TestConfig

@allure.epic("DemoQA Testing")
@allure.feature("Elements Testing")
class TestElements:
    @pytest.fixture
    def driver(self):
        driver = TestHelper.get_driver()
        driver.maximize_window()
        driver.implicitly_wait(20)
        yield driver
        driver.quit()
    
    @pytest.fixture
    def elements_page(self, driver):
        return ElementsPage(driver)
    
    @allure.story("Text Box Testing")
    def test_text_box_submission(self, driver, elements_page):
        with allure.step("Navigate to Text Box"):
            driver.get(TestConfig.BASE_URL + "/text-box")  # Direct URL navigation
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "userName"))
            )
        
        with allure.step("Fill and submit form"):
            elements_page.fill_text_box_form(TestConfig.TEST_USER)
            
        with allure.step("Verify submission"):
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "output"))
            )
            output = driver.find_element(By.ID, "output")
            assert TestConfig.TEST_USER["email"] in output.text
    
    @allure.story("Web Tables Testing")
    def test_web_table_entry(self, driver, elements_page):
        with allure.step("Navigate to Web Tables"):
            driver.get(TestConfig.BASE_URL + "/webtables")  # Direct URL navigation
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "addNewRecordButton"))
            )
        
        with allure.step("Add new record"):
            elements_page.add_web_table_entry(TestConfig.TEST_USER)
            
        with allure.step("Verify record"):
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "rt-tbody"))
            )
            table = driver.find_element(By.CLASS_NAME, "rt-tbody")
            assert TestConfig.TEST_USER["email"] in table.text