from selenium.webdriver.common.by import By
from basic_methods import BrowserWrapper 
from selenium.webdriver.common.keys import Keys

import requests

""" Тест 1 Поиск в яндексе """
def test_ya_page_tensor_search(browser):
    ya_page = BrowserWrapper(browser)
        
    """ 1) Зайти на https://ya.ru/ """
    ya_page.move_to_url('https://ya.ru/')
    
    """ 2) Проверить наличия поля поиска """
    search_input = ya_page.wait_and_return_selector((By.ID, "text"))
    assert search_input  
    
    """ 3) Ввести в поиск Тензор """
    search_input.click()
    search_input.send_keys("Тензор")
    
    """ 4) Проверить, что появилась таблица с подсказками (suggest) """
    suggest_menu = ya_page.wait_and_return_selector((By.CLASS_NAME, "mini-suggest__item"))
    assert suggest_menu  
    
    """ 5) Нажать enter """
    search_input.send_keys(Keys.ENTER)
    
    """ 6) Проверить, что появилась страница результатов поиска """
    search_results = ya_page.wait_and_return_all_by_selector((By.XPATH, "//li[contains(@class,'serp-item') ]"))
    assert len(search_results) > 0
    
    """ 7) Проверить 1 ссылка ведет на сайт tensor.ru """
    tensor_search = ya_page.wait_and_return_selector((By.XPATH, "//li[contains(@class,'serp-item') ][1]//a[contains(@class,'OrganicTitle')]"))
    href = tensor_search.get_attribute("href")
    assert str(href) == "https://tensor.ru/"
    
    
""" Тест 2 Картинки на яндексе """    
def test_pictures_bar(browser):
    ya_page = BrowserWrapper(browser)
    
    """ 1) Зайти на ya.ru """
    ya_page.move_to_url('https://ya.ru/')
    
    """ 2) Проверить, что кнопка меню присутствует на странице """
    ya_all_menu = ya_page.wait_and_return_selector((By.XPATH, "//a[contains(@title,'Все сервисы') ]"))
    assert ya_all_menu
    
    """ 3) Открыть меню, выбрать “Картинки” """
    ya_all_menu.click()
    ya_pictures = ya_page.wait_and_return_selector((
        By.XPATH, "//div[contains(@class, 'services')]//div[contains(text(), 'Картинки')]"))
    ya_pictures.click()
    
    """ 4) Проверить, что перешли на url https://yandex.ru/images/ """
    pictures_url = str(ya_page.current_url())
    assert pictures_url == "https://yandex.ru/images/"
    
    """ 5) Открыть первую категорию """
    first_picture_category = ya_page.wait_and_return_all_by_selector((
        By.XPATH, "//div[contains(@class, 'PopularRequestList')]//div[contains(@class, 'PopularRequestList')]"))[0]
    category_text = str(first_picture_category.get_attribute("data-grid-text"))
    first_picture_category.click()
    
    """ 6) Проверить, что название категории отображается в поле поиска """
    pictures_search_input = ya_page.wait_and_return_selector((
        By.XPATH, "//span[contains(@class, 'input__box')]//input[contains(@class, 'input__control')]"))
    text_pictures_search_input = pictures_search_input.get_attribute("value")
    assert category_text == text_pictures_search_input
    
    """ 7) Открыть 1 картинку """
    first_picture_to_open = ya_page.wait_and_return_all_by_selector((
        By.XPATH, "//div[contains(@class, 'serp-item__preview')]//a"))[0]
    first_picture_to_open.click() 
    first_picture = ya_page.wait_and_return_selector((
        By.XPATH, "//div[contains(@class, 'MMImage')]//img[contains(@class, 'MMImage-Origin')]"))
    ya_page.right_click(first_picture) 
    """ обратил внимание, что изначально яндекс не дает оригинальной ссылки на изображение
    и подставляет его превью в разных разрешенеиях поэтому тест может иногда не проходить. Если вызвать контекстное меню, 
    подставляется ссылка на оригинальное изображение в сети.
    Поэтому для корректной проверки картинок добавил нажатие правой кнопкой""" 
    first_picture_src = str(first_picture.get_attribute("src"))
    
    """ 8) Проверить, что картинка открылась 
    (предположил, что нужно проверить доступность картинки по ее src аттрибуту и использовал библиотеку requests,
      в требованиях ее нет, поэтому ее нужно дополнительно устанавливать в окружение и раскомментировать следующий assert ) """
    
    """ assert requests.get(first_picture_src).status_code == 200 """
    assert first_picture

    """ 9) Нажать кнопку вперед """
    switch_button_next = ya_page.wait_and_return_selector((By.XPATH, "//div[contains(@class, 'CircleButton_type_next')]"))
    switch_button_next.click()
    
    """ 10. Проверить, что картинка сменилась """
    second_picture = ya_page.wait_and_return_selector((
        By.XPATH, "//div[contains(@class, 'MMImage')]//img[contains(@class, 'MMImage-Origin')]"))
    ya_page.right_click(second_picture)
    second_picture_src = str(second_picture.get_attribute("src"))
    assert second_picture_src != first_picture_src
    
    """ 11. Нажать назад """
    switch_button_prev = ya_page.find_clickable((By.XPATH, "//div[contains(@class, 'CircleButton_type_prev')]"))
    switch_button_prev.click()
    
    """ 12. Проверить, что картинка осталась из шага 8 """
    first_picture_again = ya_page.wait_and_return_selector((By.XPATH, "//img[contains(@class, 'MMImage-Origin')]"))
    ya_page.right_click(first_picture_again)
    first_picture_again_src = str(first_picture_again.get_attribute("src"))
    
    assert first_picture_again_src == first_picture_src

    
    
        

    
    