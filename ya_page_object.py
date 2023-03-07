from basic_methods import BrowserWrapper
from selenium.webdriver.common.by import By

class selectors_for_ya_page_test:
    initial_page = 'https://ya.ru/'
    selector_ya_page_search_input = (By.ID, "text")
    selector_ya_page_search_button = (By.CLASS_NAME, "search3__button")
    selector_ya_page_menu_bar = (By.XPATH, "//a[contains(@title,'Все сервисы') ]")
    selector_ya_page_pictures = (By.XPATH, "//div[contains(@class, 'services')]//div[contains(text(), 'Картинки')]")
    selector_ya_page_search_suggest_menu = (By.CLASS_NAME, "mini-suggest__item")
    selector_ya_page_menu_bar_categories_names = (By.XPATH, "//a[contains(@class, 'services-more-popup__item')]//div[contains(@class, 'services-more-popup__item-title')]" )
    selector_ya_page_menu_bar_categories = (By.XPATH, "//a[contains(@class, 'services-more-popup__item')]")

class ya_page(BrowserWrapper):
    def insert_prase_into_search(self,phrase):
        input = self.wait_and_return_selector(selectors_for_ya_page_test.selector_ya_page_search_input)
        input.click()
        input_value = str(input.get_attribute("value"))
        if input_value != "":
            input.clear()
            input.send_keys(phrase)
        else:
            input.send_keys(phrase)

    def move_to_start_page(self):
        return self.move_to_url(selectors_for_ya_page_test.initial_page) 
    
    def check_input_persistance(self):
        return self.wait_and_return_selector(selectors_for_ya_page_test.selector_ya_page_search_input)

    def search_suggest_persistance_by_phrase(self, phrase_to_search):
        self.insert_prase_into_search(phrase_to_search)
        return self.wait_and_return_selector(selectors_for_ya_page_test.selector_ya_page_search_suggest_menu)

    def start_search_with_phrase(self, phrase_to_search):

        self.insert_prase_into_search(phrase_to_search)
        search_button = self.wait_and_return_selector(selectors_for_ya_page_test.selector_ya_page_search_button)
        search_button.click()

    def menu_bar_persistance(self):
        return self.wait_and_return_selector(selectors_for_ya_page_test.selector_ya_page_menu_bar)
    
    def menu_bar_open(self):
        menu_bar = self.menu_bar_persistance()
        return menu_bar.click()
    
    def menu_bar_open_category(self, category_name):
        menu_catyegories_list = self.wait_and_return_all_by_selector(selectors_for_ya_page_test.selector_ya_page_menu_bar_categories_names)
        
        for idx,x in enumerate(menu_catyegories_list) :
            x_text = x.text
            if category_name == x_text:
                menu_catyegories_list[idx].click()
                
