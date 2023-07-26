import allure
import pytest
from pages.order_page import OrderPage
from url import Urls
from data import Registration
from data import PhoneNumber
from data import Date
from data import TextData, RentalData
from data import IncorrectData

@pytest.mark.usefixtures("driver")
class TestOrderButton:

    @allure.title('Оформление заказа по кнопке "Заказать" в шапке страницы')
    def test_order_button_on_header_passed(self, driver):

        order = OrderPage(driver)
        order.open_page(Urls.MAIN_PAGE)
        order.click_order_button_in_header()
        order.filling_form(Registration.fake_person_info(), PhoneNumber.get_phone_number())
        order.wait_for_rent_form()
        order.input_rental_information(Date.get_date_today(), RentalData.RENTAL_DATA_1)
        order.wait_for_confirm()
        order.click_confirmation_order()
        order_title = order.get_new_order_title()
        order.wait_for_order_completed()

        assert TextData.SUCCESSFUL_ORDER_TEXT in order_title

    @allure.title('Оформить заказ по кнопке "Заказать" внизу страницы')
    def test_order_page_correct_user_data_passed(self, driver):

        order = OrderPage(driver)
        order.open_page(Urls.MAIN_PAGE)
        order.scroll_to_order_button()
        order.click_order_button_in_bottom()
        order.filling_form(Registration.fake_person_info(), PhoneNumber.get_phone_number())
        order.wait_for_rent_form()
        order.input_rental_information(Date.get_date_tomorrow(), RentalData.RENTAL_DATA_2)
        order.wait_for_confirm()
        order.click_confirmation_order()
        order_title = order.get_new_order_title()
        order.wait_for_order_completed()

        assert TextData.SUCCESSFUL_ORDER_TEXT in order_title

    @allure.title('Оформление заказа с некорректными данными')
    @allure.description('Некорректное Имя пользователя')
    def test_order_page_first_name_incorrect_show_error_message_failed(self, driver):

        order = OrderPage(driver)
        order.open_page(Urls.MAIN_PAGE)
        order.click_order_button_in_header()
        order.filling_incorrect_form(IncorrectData.INCORRECT_FIRSTNAME, PhoneNumber.get_phone_number())
        firstname_error_text = order.wait_for_error_message_firstname()

        assert firstname_error_text == TextData.FIRSTNAME_ERROR

    @allure.title('Оформление заказа с некорректными данными')
    @allure.description('Некорректная Фамилия пользователя')
    def test_order_page_last_name_incorrect_show_error_message_failed(self, driver):

        order = OrderPage(driver)
        order.open_page(Urls.MAIN_PAGE)
        order.click_order_button_in_header()
        order = OrderPage(driver)
        order.filling_incorrect_form(IncorrectData.INCORRECT_LASTNAME, PhoneNumber.get_phone_number())
        lastname_error_text = order.wait_for_error_message_lastname()

        assert lastname_error_text == TextData.LASTNAME_ERROR

    @allure.title('Оформление заказа с некорректными данными')
    @allure.description('Некорректный адрес пользователя')
    def test_order_page_address_incorrect_show_error_message_failed(self, driver):

        order = OrderPage(driver)
        order.open_page(Urls.MAIN_PAGE)
        order.click_order_button_in_header()
        order = OrderPage(driver)
        order.filling_incorrect_form(IncorrectData.INCORRECT_ADDRESS, PhoneNumber.get_phone_number())
        address_error_text = order.wait_for_error_message_address()

        assert address_error_text == TextData.ADDRESS_ERROR

    @allure.title('Оформление заказа с некорректными данными')
    @allure.description('Некорректный номер телефона пользователя')
    def test_order_page_phone_number_incorrect_show_error_message_failed(self, driver):

        order = OrderPage(driver)
        order.open_page(Urls.MAIN_PAGE)
        order.click_order_button_in_header()
        order = OrderPage(driver)
        order.filling_incorrect_form(Registration.fake_person_info(), PhoneNumber.get_incorrect_phone_number())
        phonenumber_error_text = order.wait_for_error_message_phonenumber()

        assert phonenumber_error_text == TextData.PHONENUMBER_ERROR