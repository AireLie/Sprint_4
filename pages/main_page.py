import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.main_page_locators import MainPageLocators

class MainPage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Нажать и принять все куки')
    def click_cookie_button(self):
        self.driver.find_element(*MainPageLocators.COOKIES_BUTTON).click()

    @allure.step('Скролл до раздела "Вопросы о важном"')
    def scroll_to_questions(self):
        faq = self.driver.find_element(*MainPageLocators.LOCATOR_FAQ)
        self.driver.execute_script("arguments[0].scrollIntoView();", faq)
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(MainPageLocators.LOCATOR_FAQ))

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
        button = self.driver.find_element(*MainPageLocators.ORDER_BUTTON_MAIN_PAGE)
        self.driver.execute_script("arguments[0].scrollIntoView();", button)
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(MainPageLocators.ORDER_BUTTON_MAIN_PAGE))

    @allure.step('Нажать на кнопку "Заказать" внизу страницы')
    def click_order_button(self):
        self.driver.find_element(*MainPageLocators.ORDER_BUTTON_MAIN_PAGE).click()

    @allure.step('Текст заголовка главной страницы')
    def get_main_header_text(self):
        return self.driver.find_element(*MainPageLocators.HEADER_TEXT).text

    @allure.step('Нажать на кнопку "Заказать" в шапке')
    def click_order_button_in_header(self):
        self.driver.find_element(*MainPageLocators.HEADER_ORDER_BUTTON).click()