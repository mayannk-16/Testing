from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
        self.actions = ActionChains(driver)

    def find_element(self, locator):
        try:
            return self.wait.until(EC.presence_of_element_located(locator))
        except TimeoutException:
            self.scroll_to_top()  # DemoQA sometimes needs scroll reset
            return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator):
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            self.scroll_into_view(element)
            element.click()
        except ElementClickInterceptedException:
            element = self.find_element(locator)
            self.driver.execute_script("arguments[0].click();", element)

    def type(self, locator, text):
        element = self.find_element(locator)
        self.scroll_into_view(element)
        element.clear()
        element.send_keys(text)

    def scroll_into_view(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("window.scrollBy(0, -100);")  # Adjust for fixed header

    def scroll_to_top(self):
        self.driver.execute_script("window.scrollTo(0, 0);")

    def get_text(self, locator):
        return self.find_element(locator).text