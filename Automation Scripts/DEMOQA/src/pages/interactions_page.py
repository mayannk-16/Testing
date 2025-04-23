from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class InteractionsPage(BasePage):
    # Locators
    DRAGABBLE = (By.ID, "dragBox")
    SORTABLE_ITEMS = (By.CSS_SELECTOR, ".list-group-item")

    def get_draggable_position(self):
        element = self.find_element(self.DRAGABBLE)
        return element.location

    def drag_element(self, x_offset, y_offset):
        source = self.find_element(self.DRAGABBLE)
        actions = ActionChains(self.driver)
        actions.drag_and_drop_by_offset(source, x_offset, y_offset).perform()

    def get_sortable_items_order(self):
        items = self.driver.find_elements(*self.SORTABLE_ITEMS)
        return [item.text for item in items]

    def move_item(self, from_index, to_index):
        items = self.driver.find_elements(*self.SORTABLE_ITEMS)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(items[from_index], items[to_index]).perform()