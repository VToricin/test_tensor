from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


class BrowserWrapper:
    
    def __init__(self, driver):
        self.driver = driver

    def move_to_url(self, url_to_move):
        return self.driver.get(url_to_move)

    def wait_and_return_selector(self, selector, time = 5):
        return WebDriverWait(self.driver, time).until(
            expected_conditions.presence_of_element_located(selector))

    def wait_and_return_all_by_selector(self, selector, time = 5):
        return WebDriverWait(self.driver, time).until(
            expected_conditions.presence_of_all_elements_located(selector))
    
    def find_clickable(self, selector, time = 5):
        return WebDriverWait(self.driver, time).until(
            expected_conditions.element_to_be_clickable(selector))
           

    def current_url(self, time = 5):
        
        
        self.driver.switch_to.window(self.driver.window_handles[-1])
        return self.driver.current_url
    
    def right_click(self, webelement):

        return ActionChains(self.driver).context_click(webelement).perform()
        