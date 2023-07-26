import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.main_page_locators import MainPageLocators
from locators.base_page_locators import BasePageLocators
from pages.base_page import BasePage

class MainPage(BasePage):


    @allure.step('Нажать на логотип "Яндекс"')
    def click_yandex_logo(self):
        self.driver.find_element(*BasePageLocators.YANDEX_LOGO).click()

    @allure.step('Нажать на логотип "Самокат"')
    def click_scooter_logo(self):
        self.driver.find_element(*BasePageLocators.SCOOTER_LOGO).click()

    @allure.step('Нажать и принять все куки')
    def click_cookie_button(self):
        self.driver.find_element(*MainPageLocators.COOKIES_BUTTON).click()

    @allure.step('Скролл до раздела "Вопросы о важном"')
    def scroll_to_questions(self):
        self.scroll_to(MainPageLocators.LOCATOR_FAQ)


    def get_questions(self):
        return self.driver.find_elements(*MainPageLocators.LOCATOR_QUESTIONS)

    @allure.step('Нажать на вопрос')
    def click_on_question(self, index):
        questions = self.get_questions()
        questions[index - 1].click()

    @allure.step('Получить ответ')
    def get_answer_text(self):
        return self.driver.find_element(*MainPageLocators.LOCATOR_ANSWER).text

    def wait_for_get_answer(self):
        WebDriverWait(self.driver, 25).until(expected_conditions.visibility_of_element_located(MainPageLocators.LOCATOR_ANSWER))

    @allure.step('Скролл до кнопки "Заказать" на странице')
    def scroll_to_order_button(self):
        self.scroll_to(MainPageLocators.ORDER_BUTTON_MAIN_PAGE)

    @allure.step('Нажать на кнопку "Заказать" внизу страницы')
    def click_order_button_in_bottom(self):
        self.driver.find_element(*MainPageLocators.ORDER_BUTTON_MAIN_PAGE).click()

    @allure.step('Текст заголовка главной страницы')
    def get_main_header_text(self):
        return self.driver.find_element(*MainPageLocators.HEADER_TEXT).text

    @allure.step('Нажать на кнопку "Заказать" в шапке')
    def click_order_button_in_header(self):
        self.driver.find_element(*MainPageLocators.HEADER_ORDER_BUTTON).click()