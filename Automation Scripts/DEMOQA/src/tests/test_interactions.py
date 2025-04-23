import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.pages.interactions_page import InteractionsPage
from src.utils.test_helper import TestHelper
from src.config.config import TestConfig

@allure.epic("DemoQA Testing")
@allure.feature("Interactions Testing")
class TestInteractions:
    @pytest.fixture
    def driver(self):
        driver = TestHelper.get_driver()
        driver.maximize_window()
        driver.implicitly_wait(20)
        yield driver
        driver.quit()

    @pytest.fixture
    def interactions_page(self, driver):
        return InteractionsPage(driver)

    @allure.story("Draggable Testing")
    def test_draggable(self, driver, interactions_page):
        with allure.step("Navigate to Draggable"):
            driver.get(TestConfig.BASE_URL + "/dragabble")
            
        with allure.step("Perform drag operation"):
            initial_position = interactions_page.get_draggable_position()
            interactions_page.drag_element(100, 100)
            final_position = interactions_page.get_draggable_position()
            assert final_position != initial_position

    @allure.story("Sortable Testing")
    def test_sortable(self, driver, interactions_page):
        with allure.step("Navigate to Sortable"):
            driver.get(TestConfig.BASE_URL + "/sortable")
            
        with allure.step("Perform sort operation"):
            initial_order = interactions_page.get_sortable_items_order()
            interactions_page.move_item(0, 3)
            final_order = interactions_page.get_sortable_items_order()
            assert final_order != initial_order