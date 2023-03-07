from basic_methods import BrowserWrapper
from selenium.webdriver.common.by import By


class selectors_for_ya_search_page_result:
    selector_search_result = (By.XPATH, "//li[contains(@class,'serp-item')]//a[contains(@class,'OrganicTitle')]")
    selector_search_result_by_order = (By.XPATH, "//li[contains(@class,'serp-item') ]")
    selector_result_by_order = (By.XPATH, "//a[contains(@accesskey)]")

class ya_search_page_result(BrowserWrapper):
    def return_search_results(self):
        list = self.wait_and_return_all_by_selector(selectors_for_ya_search_page_result.selector_search_result)
        return list     
    
    def results_persistance(self):
        search_results_list = self.return_search_results()
        
        if len(search_results_list) > 0:
            return True
        else:
            return False
        
    def check_result_url_by_order_number(self, order_number):
        result = self.return_search_results()[order_number - 1]
        return str(result.get_attribute("href"))