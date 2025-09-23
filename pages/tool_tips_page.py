

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class Tooltipspage:
   
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demoqa.com/tool-tips"
        self.show_message_button = (By.ID, "toolTipButton")
        self.show_message_text = (By.ID, "toolTipTextField")
        self.actions = ActionChains(self.driver)
        self.tooltip = self.driver.find_element(By.CLASS_NAME, "tooltip-inner")
        
    def navigate(self):
        self.driver.get(self.url)  

    def move_to_button(self):
        self.actions.move_to_element(self.driver.find_element(*self.show_message_button)).perform()
        

    def move_to_text(self):
        self.actions.move_to_element(self.driver.find_element(*self.show_message_text)).perform()





    