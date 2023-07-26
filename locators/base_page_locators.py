from selenium.webdriver.common.by import By

class BasePageLocators:
    YANDEX_LOGO = By.XPATH, "//*[@alt='Yandex']"  # Лого "Яндекс"
    SCOOTER_LOGO = By.XPATH, "//*[@alt='Scooter']"  # Лого "Самокат"

