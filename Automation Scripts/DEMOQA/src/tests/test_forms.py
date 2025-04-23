import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.pages.forms_page import FormsPage
from src.utils.test_helper import TestHelper
from src.config.config import TestConfig

@allure.epic("DemoQA Testing")
@allure.feature("Forms Testing")
class TestForms:
    @pytest.fixture
    def driver(self):
        driver = TestHelper.get_driver()
        driver.maximize_window()
        driver.implicitly_wait(20)
        yield driver
        driver.quit()

    @pytest.fixture
    def forms_page(self, driver):
        return FormsPage(driver)

    @allure.story("Practice Form Testing")
    def test_submit_practice_form(self, driver, forms_page):
        with allure.step("Navigate to Practice Form"):
            driver.get(TestConfig.BASE_URL + "/automation-practice-form")
            
        with allure.step("Fill and submit form"):
            forms_page.fill_practice_form(
                TestConfig.TEST_USER,
                TestConfig.FORM_DATA
            )
            
        with allure.step("Verify submission"):
            modal = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "modal-content"))
            )
            assert TestConfig.TEST_USER["email"] in modal.text