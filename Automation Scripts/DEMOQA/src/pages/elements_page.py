from .base_page import BasePage
from selenium.webdriver.common.by import By

class ElementsPage(BasePage):
    # Navigation
    ELEMENTS_SECTION = (By.XPATH, "//h5[text()='Elements']")
    TEXT_BOX_MENU = (By.XPATH, "//span[text()='Text Box']")
    WEB_TABLES_MENU = (By.XPATH, "//span[text()='Web Tables']")
    
    # Text Box
    FULL_NAME_INPUT = (By.ID, "userName")
    EMAIL_INPUT = (By.ID, "userEmail")
    CURRENT_ADDRESS_INPUT = (By.ID, "currentAddress")
    PERMANENT_ADDRESS_INPUT = (By.ID, "permanentAddress")
    SUBMIT_BTN = (By.ID, "submit")
    
    # Web Tables
    ADD_BUTTON = (By.ID, "addNewRecordButton")
    REGISTRATION_FORM = {
        "firstName": (By.ID, "firstName"),
        "lastName": (By.ID, "lastName"),
        "email": (By.ID, "userEmail"),
        "age": (By.ID, "age"),
        "salary": (By.ID, "salary"),
        "department": (By.ID, "department")
    }
    
    def navigate_to_elements(self):
        self.click(self.ELEMENTS_SECTION)
        
    def navigate_to_text_box(self):
        self.click(self.TEXT_BOX_MENU)
        
    def navigate_to_web_tables(self):
        self.click(self.WEB_TABLES_MENU)
        
    def fill_text_box_form(self, user_data):
        self.type(self.FULL_NAME_INPUT, f"{user_data['first_name']} {user_data['last_name']}")
        self.type(self.EMAIL_INPUT, user_data['email'])
        self.type(self.CURRENT_ADDRESS_INPUT, user_data['current_address'])
        self.type(self.PERMANENT_ADDRESS_INPUT, user_data['permanent_address'])
        self.click(self.SUBMIT_BTN)
        
    def add_web_table_entry(self, user_data):
        self.click(self.ADD_BUTTON)
        for field, locator in self.REGISTRATION_FORM.items():
            if field == "firstName":
                self.type(locator, user_data["first_name"])
            elif field == "lastName":
                self.type(locator, user_data["last_name"])
            else:
                self.type(locator, user_data[field])
        self.click(self.SUBMIT_BTN)