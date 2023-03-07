from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions


from selenium.webdriver import ActionChains


class BrowserWrapper:
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def move_to_url(self, url_to_move):
        return self.driver.get(url_to_move)

    def wait_and_return_selector(self, selector):
        return self.wait.until(
            expected_conditions.presence_of_element_located(selector))

    def wait_and_return_all_by_selector(self, selector):
        return self.wait.until(
            expected_conditions.presence_of_all_elements_located(selector))
    
    def get_current_url(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])
        return str(self.driver.current_url)
    
    def right_click(self, webelement):
        return ActionChains(self.driver).context_click(webelement).perform()
        