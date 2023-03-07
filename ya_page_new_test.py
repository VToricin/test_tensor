from ya_page_object import ya_page
from ya_search_results_page_object import ya_search_page_result
from ya_images_page_object import ya_images
import time 

class initial_test_data:
    word_for_search = "Тензор"
    order_number_of_search_result_toCheck = 1
    link_to_compare_with_search_result = "https://tensor.ru/"

    category_to_search_in_ya_bar = "Картинки"
    url_of_picked_category = "https://yandex.ru/images/"
    image_category_to_open = 1
    order_number_of_picture_to_open_first = 1

def test_ya_page(browser):
    ya_page_new_object = ya_page(browser)
    ya_page_new_object.move_to_start_page()
    assert ya_page_new_object.check_input_persistance()
    assert ya_page_new_object.search_suggest_persistance_by_phrase(initial_test_data.word_for_search)
    ya_page_new_object.start_search_with_phrase(initial_test_data.word_for_search)
    ya_search_page_object = ya_search_page_result(browser)
    assert ya_search_page_object.results_persistance()
    assert ya_search_page_object.check_result_url_by_order_number(
        initial_test_data.order_number_of_search_result_toCheck) == initial_test_data.link_to_compare_with_search_result

def test_ya_pictures(browser):
    ya_page_new_object = ya_page(browser)
    ya_page_new_object.move_to_start_page()
    assert ya_page_new_object.menu_bar_persistance()
    ya_page_new_object.menu_bar_open()
    ya_page_new_object.menu_bar_open_category(initial_test_data.category_to_search_in_ya_bar) 
    assert ya_page_new_object.get_current_url() == initial_test_data.url_of_picked_category
    ya_image_page_new_object = ya_images(browser)
    ya_image_page_new_object.open_category_by_number(initial_test_data.image_category_to_open)
    assert ya_image_page_new_object.check_category_name_in_search_field()
    ya_image_page_new_object.open_image_by_number(initial_test_data.order_number_of_picture_to_open_first)
    ya_image_page_new_object.next_image_button_press()
    assert ya_image_page_new_object.compare_last_shown_image_with_previous()
    ya_image_page_new_object.prev_image_button_press()
    assert ya_image_page_new_object.compare_last_shown_image_with_first_shown()
    time.sleep(3) 