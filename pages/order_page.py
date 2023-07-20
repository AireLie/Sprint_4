import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.common.keys import Keys

class OrderPage:

    def __init__(self, driver):
        self.driver = driver

    def set_first_name(self, firstname):
        self.driver.find_element(*OrderPageLocators.LOCATOR_NAME).send_keys(firstname)

    def set_last_name(self, lastname):
        self.driver.find_element(*OrderPageLocators.LOCATOR_LAST_NAME).send_keys(lastname)

    def set_address(self, address):
        self.driver.find_element(*OrderPageLocators.LOCATOR_ADDRESS).send_keys(address)

    def set_subway_station(self, station):
        self.driver.find_element(*OrderPageLocators.LOCATOR_STATION).send_keys(station)
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(OrderPageLocators.STATION_DROPDOWN))
        self.driver.find_element(*OrderPageLocators.STATION_DROPDOWN).click()
        WebDriverWait(self.driver, 10).until(expected_conditions.invisibility_of_element(OrderPageLocators.STATION_DROPDOWN))

    def set_phone_number(self, number):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(OrderPageLocators.LOCATOR_PHONE_NUMBER))
        self.driver.find_element(*OrderPageLocators.LOCATOR_PHONE_NUMBER).send_keys(number)

    def click_next_button(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(OrderPageLocators.NEXT_BUTTON))
        self.driver.find_element(*OrderPageLocators.NEXT_BUTTON).click()

    @allure.step('Заполнить поля раздела "Для кого самокат?"')
    def filling_form(self, person, number):
        self.set_first_name(person.get('firstname'))
        self.set_last_name(person.get('lastname'))
        self.set_address(person.get('address'))
        self.set_subway_station(person.get('subway_station'))
        self.set_phone_number(number)
        self.click_next_button()

    @allure.step('Заполнить некорректно поля раздела "Для кого самокат?"')
    def filling_incorrect_form(self, incorrect_data, number):
        self.set_first_name(incorrect_data.get('firstname'))
        self.set_last_name(incorrect_data.get('lastname'))
        self.set_address(incorrect_data.get('address'))
        self.set_subway_station(incorrect_data.get('subway_station'))
        self.set_phone_number(number)
        self.click_next_button()

    def wait_for_rent_form(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(OrderPageLocators.RENT_FORM))

    def set_date(self, date):
        self.driver.find_element(*OrderPageLocators.LOCATOR_DATE).send_keys(date)
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(OrderPageLocators.LOCATOR_CALENDAR))
        self.driver.find_element(*OrderPageLocators.LOCATOR_DATE).send_keys(Keys.ENTER)
        WebDriverWait(self.driver, 10).until(expected_conditions.invisibility_of_element(OrderPageLocators.LOCATOR_CALENDAR))

    def select_rental_period(self, period):
        self.driver.find_element(*OrderPageLocators.RENTAL_PERIOD).click()
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(OrderPageLocators.RENTAL_PERIOD_DROPDOWN))
        self.driver.find_element(*period).click()
        WebDriverWait(self.driver, 10).until(expected_conditions.invisibility_of_element(OrderPageLocators.RENTAL_PERIOD_DROPDOWN))

    def click_checkbox(self, color):
        self.driver.find_element(*color).click()

    def set_comment(self, comment):
        self.driver.find_element(*OrderPageLocators.LOCATOR_COMMENT).send_keys(comment)

    def click_order_button(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(OrderPageLocators.ORDER_BUTTON))
        self.driver.find_element(*OrderPageLocators.ORDER_BUTTON).click()

    @allure.step('Заполнить раздел "Про аренду"')
    def input_rental_information(self, date, rent_data):
        color_checkbox = {"black": OrderPageLocators.LOCATOR_BLACK_CHECKBOX, "grey": OrderPageLocators.LOCATOR_GREY_CHECKBOX}
        day_period = {"one": OrderPageLocators.LOCATOR_ONE_DAY, "two": OrderPageLocators.LOCATOR_TWO_DAY}
        self.set_date(date)
        self.select_rental_period(day_period.get(rent_data.get('rental_period')))
        self.click_checkbox(color_checkbox.get(rent_data.get('scooter_color')))
        self.set_comment(rent_data.get('comment'))
        self.click_order_button()

    def wait_for_confirm(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(OrderPageLocators.LOCATOR_CONFIRM))

    @allure.step('Клик по кнопке "Да"')
    def click_confirmation_order(self):
        self.driver.find_element(*OrderPageLocators.YES_BUTTON).click()

    def wait_for_order_completed(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(OrderPageLocators.ORDER_COMPLETED))

    @allure.step('Успешный заказ')
    def get_new_order_title(self):
        new_order_text = self.driver.find_element(*OrderPageLocators.ORDER_COMPLETED).text
        return new_order_text

    def click_order_status_button(self):
        self.driver.find_element(*OrderPageLocators.ORDER_STATUS_BUTTON).click()

    @allure.step('Ошибка при вводе некорректного имени')
    def wait_for_error_message_firstname(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(OrderPageLocators.INCORRECT_FIRST_NAME_MESSAGE))
        firstname_error_text = self.driver.find_element(*OrderPageLocators.INCORRECT_FIRST_NAME_MESSAGE).text
        return firstname_error_text

    @allure.step('Ошибка при вводе некорректной фамилии')
    def wait_for_error_message_lastname(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(OrderPageLocators.INCORRECT_LAST_NAME_MESSAGE))
        lastname_error_text = self.driver.find_element(*OrderPageLocators.INCORRECT_LAST_NAME_MESSAGE).text
        return lastname_error_text

    @allure.step('Ошибка при вводе некорректного адреса')
    def wait_for_error_message_address(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(OrderPageLocators.INCORRECT_ADDRESS_MESSAGE))
        address_error_text = self.driver.find_element(*OrderPageLocators.INCORRECT_ADDRESS_MESSAGE).text
        return address_error_text

    @allure.step('Ошибка при вводе некорректного номера телефона')
    def wait_for_error_message_phonenumber(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(OrderPageLocators.INCORRECT_PHONENUMBER_MESSAGE))
        phonenumber_error_text = self.driver.find_element(*OrderPageLocators.INCORRECT_PHONENUMBER_MESSAGE).text
        return phonenumber_error_text