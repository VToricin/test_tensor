from basic_methods import BrowserWrapper
from selenium.webdriver.common.by import By


class selectors_for_ya_images_page:
    selector_ya_images_pictures_list = (By.XPATH, "//div[contains(@class, 'serp-item__preview')]//a")
    selector_ya_images_categories_list = (
        By.XPATH, "//div[contains(@class, 'PopularRequestList')]//div[contains(@class, 'PopularRequestList')]")
    selector_ya_images_input = (By.XPATH, "//span[contains(@class, 'input__box')]//input[contains(@class, 'input__control')]")
    selector_ya_images_next_image_button = (By.XPATH, "//div[contains(@class, 'CircleButton_type_next')]")
    selector_ya_images_picked_image = (By.XPATH, "//div[contains(@class, 'MMImage')]//img[contains(@class, 'MMImage-Origin')]")
    selector_ya_images_prev_image_button = (By.XPATH, "//div[contains(@class, 'CircleButton_type_prev')]")

class ya_images(BrowserWrapper):
    image_sources = []
    
    def image_src_check_and_save(self):
        image = self.wait_and_return_selector(
            selectors_for_ya_images_page.selector_ya_images_picked_image)
        self.right_click(image) 
        image_src = image.get_attribute("src")
        self.image_sources.append(image_src)

    def open_image_by_number(self, image_number):
        image = self.wait_and_return_all_by_selector(
            selectors_for_ya_images_page.selector_ya_images_pictures_list)[image_number - 1]
        image.click()
        self.image_src_check_and_save()

    def compare_last_shown_image_with_previous(self):
        return True if self.image_sources[-1] != self.image_sources[len(self.image_sources)-2] else False
        
    def compare_last_shown_image_with_first_shown(self):
        return True if self.image_sources[-1] == self.image_sources[0] else False
       
    
    def open_category_by_number(self, category_number):
        category_to_click = self.wait_and_return_all_by_selector(
            selectors_for_ya_images_page.selector_ya_images_categories_list)[category_number - 1]
        self.last_category_clicked_name = str(category_to_click.get_attribute("data-grid-text"))
        category_to_click.click()   

    def check_category_name_in_search_field(self):
        input = self.wait_and_return_selector(selectors_for_ya_images_page.selector_ya_images_input)
        input_value = str(input.get_attribute("value"))
        if input_value == self.last_category_clicked_name:
            return True
        else:
            return False
        
    def next_image_button_press(self):
        next_image_button = self.wait_and_return_selector(selectors_for_ya_images_page.selector_ya_images_next_image_button)
        next_image_button.click()
        self.image_src_check_and_save()

    def prev_image_button_press(self):
        prev_image_button = self.wait_and_return_selector(selectors_for_ya_images_page.selector_ya_images_prev_image_button)
        prev_image_button.click()
        self.image_src_check_and_save()
