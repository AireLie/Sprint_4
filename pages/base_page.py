import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_new_tab(self, number):
        WebDriverWait(self.driver, 10).until(expected_conditions.number_of_windows_to_be(number))

    def wait_for_page_load(self, url):
        WebDriverWait(self.driver, 20).until(expected_conditions.url_to_be(url))

    @allure.step('Открыть страницу {page}')
    def open_page(self, page):
        self.driver.get(page)


    def scroll_to(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(*element))
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(element))
