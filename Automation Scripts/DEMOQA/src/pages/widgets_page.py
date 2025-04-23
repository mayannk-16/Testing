from .base_page import BasePage
from selenium.webdriver.common.by import By

class WidgetsPage(BasePage):
    # Locators
    ACCORDION_SECTION = "//div[@class='card'][{}]//div[@class='card-header']"
    ACCORDION_CONTENT = "//div[@class='card'][{}]//div[@class='card-body']"
    DATE_PICKER = (By.ID, "datePickerMonthYearInput")

    def click_accordion_section(self, section_number):
        locator = (By.XPATH, self.ACCORDION_SECTION.format(section_number))
        self.click(locator)

    def is_accordion_content_visible(self, section_number):
        locator = (By.XPATH, self.ACCORDION_CONTENT.format(section_number))
        return self.find_element(locator).is_displayed()

    def set_date(self, date_string):
        date_picker = self.find_element(self.DATE_PICKER)
        self.driver.execute_script(
            f"arguments[0].value = '{date_string}';", date_picker)

    def get_date(self):
        return self.find_element(self.DATE_PICKER).get_attribute("value")