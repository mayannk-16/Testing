from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

class FormsPage(BasePage):
    # Locators
    FIRST_NAME = (By.ID, "firstName")
    LAST_NAME = (By.ID, "lastName")
    EMAIL = (By.ID, "userEmail")
    GENDER_MALE = (By.CSS_SELECTOR, "label[for='gender-radio-1']")
    MOBILE = (By.ID, "userNumber")
    # Add date picker locators
    DATE_OF_BIRTH = (By.ID, "dateOfBirthInput")
    DATE_PICKER_MONTH = (By.CLASS_NAME, "react-datepicker__month-select")
    DATE_PICKER_YEAR = (By.CLASS_NAME, "react-datepicker__year-select")
    DATE_PICKER_DAY = "react-datepicker__day--{:03d}"

    SUBJECTS = (By.ID, "subjectsInput")
    HOBBIES_SPORTS = (By.CSS_SELECTOR, "label[for='hobbies-checkbox-1']")
    HOBBIES_READING = (By.CSS_SELECTOR, "label[for='hobbies-checkbox-2']")
    HOBBIES_MUSIC = (By.CSS_SELECTOR, "label[for='hobbies-checkbox-3']")
    SUBMIT = (By.ID, "submit")

    # Add modal verification locators
    MODAL_CONTENT = (By.CLASS_NAME, "modal-content")
    MODAL_BODY = (By.CLASS_NAME, "modal-body")
    CLOSE_MODAL = (By.ID, "closeLargeModal")

    def fill_practice_form(self, user_data, form_data):
        self.type(self.FIRST_NAME, user_data["first_name"])
        self.type(self.LAST_NAME, user_data["last_name"])
        self.type(self.EMAIL, user_data["email"])
        self.click(self.GENDER_MALE)
        self.type(self.MOBILE, form_data["mobile"])
        
        # Set date of birth
        self.set_date_of_birth("15", "July", "1990")
        
        # Fill subjects with improved handling
        for subject in form_data["subjects"]:
            subject_input = self.find_element(self.SUBJECTS)
            subject_input.send_keys(subject)
            self.wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, f"//div[contains(@class, 'subjects-auto-complete__option') and contains(text(), '{subject}')]")
                )
            ).click()
            subject_input.send_keys(Keys.TAB)
        
        # Select hobbies
        for hobby in form_data["hobbies"]:
            if hobby == "Sports":
                self.click(self.HOBBIES_SPORTS)
            elif hobby == "Reading":
                self.click(self.HOBBIES_READING)
            elif hobby == "Music":
                self.click(self.HOBBIES_MUSIC)
        
        # Submit form using JavaScript due to fixed footer
        submit_button = self.find_element(self.SUBMIT)
        self.driver.execute_script("arguments[0].click();", submit_button)
        
        # Scroll to bottom before submit
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        # Submit form with retry
        try:
            submit_button = self.find_element(self.SUBMIT)
            self.driver.execute_script("arguments[0].click();", submit_button)
        except:
            # Retry submit if first attempt fails
            self.driver.execute_script("document.getElementById('submit').click();")
        
        # Wait for modal and verify
        self.wait.until(EC.visibility_of_element_located(self.MODAL_CONTENT))
        modal_text = self.find_element(self.MODAL_BODY).text
        
        # Close modal
        close_button = self.find_element(self.CLOSE_MODAL)
        self.driver.execute_script("arguments[0].click();", close_button)
        
        return modal_text

    def set_date_of_birth(self, day, month, year):
        # Click to open date picker
        self.click(self.DATE_OF_BIRTH)
        
        # Select month
        month_dropdown = self.find_element(self.DATE_PICKER_MONTH)
        month_dropdown.click()
        month_option = self.driver.find_element(By.XPATH, f"//option[text()='{month}']")
        month_option.click()
        
        # Select year
        year_dropdown = self.find_element(self.DATE_PICKER_YEAR)
        year_dropdown.click()
        year_option = self.driver.find_element(By.XPATH, f"//option[text()='{year}']")
        year_option.click()
        
        # Select day
        day_class = self.DATE_PICKER_DAY.format(int(day))
        day_element = self.driver.find_element(By.CLASS_NAME, day_class)
        day_element.click()