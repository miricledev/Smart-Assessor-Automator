

from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

class UIControls:
    def __init__(self, driver):
        self.driver = driver
    ## Accessing the drop-down menus and selecting correct option
    def access_dd(self, option_value, search_item):
        dropdown_element = self.driver.find_element(By.ID, search_item)
        choices = Select(dropdown_element)
        choices.select_by_visible_text(option_value)
        
    ## Putting text in the text fields using ID ref
    def write_text_by_id(self, text, search_item):
        field = self.driver.find_element(By.ID, search_item)
        field.send_keys(text)
        
    ## Clicking the add button to open the form
    def btn_click_by_class(self, search_item):
        button = self.driver.find_element(By.CLASS_NAME, search_item)
        self.driver.execute_script("arguments[0].click();", button)
        