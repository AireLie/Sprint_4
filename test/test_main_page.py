import allure
import pytest
from pages.main_page import MainPage
from url import Urls
from data import TextData

@pytest.mark.usefixtures("driver")
class TestLogo:

    @allure.title('Открытие сайта Самоката по логотипу "Самокат"')
    def test_main_page_open_by_scooter_logo_passed(self, driver):

        page = MainPage(driver)
        page.open_page(Urls.ORDER_PAGE)
        page.click_scooter_logo()
        page.wait_for_page_load(Urls.MAIN_PAGE)
        current_header_text = page.get_main_header_text()
        header_text = TextData.HEADER_TEXT

        assert driver.current_url == Urls.MAIN_PAGE and header_text == current_header_text

    @allure.title('Открытие сайта Дзен по логотипу "Яндекс"')
    def test_dzen_page_open_by_yandex_logo_passed(self, driver):

        page = MainPage(driver)
        page.open_page(Urls.ORDER_PAGE)
        page.click_yandex_logo()
        page.wait_for_new_tab(2)
        driver.switch_to.window(driver.window_handles[1])
        page.wait_for_page_load(Urls.DZEN_HOME_PAGE)

        assert driver.current_url == Urls.DZEN_HOME_PAGE