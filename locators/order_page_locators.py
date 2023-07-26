from selenium.webdriver.common.by import By

class OrderPageLocators:
    LOCATOR_NAME = By.XPATH, "//input[@placeholder='* Имя']"  # Поле ввода имени
    LOCATOR_LAST_NAME = By.XPATH, "//input[@placeholder='* Фамилия']"  # Поле ввода фамилии
    LOCATOR_ADDRESS = By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"  # Поле ввода адреса
    LOCATOR_STATION = By.XPATH, "//input[@placeholder='* Станция метро']"  # Поле выбора метро
    STATION_DROPDOWN = By.XPATH, "//div[contains(@class, 'select-search__select')]/ul/li"  # Список метро
    LOCATOR_PHONE_NUMBER = By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"  # Поле ввода номера
    NEXT_BUTTON = By.XPATH, "//button[text()='Далее']"  # Кнопка "Далее"

    RENT_FORM = By.XPATH, "//div[text()='Про аренду']"  # Раздел "Про аренду"
    LOCATOR_DATE = By.XPATH, "//input[@placeholder='* Когда привезти самокат']"  # Поле ввода даты
    LOCATOR_CALENDAR = By.XPATH, "//div[@class='react-datepicker']"  # Календарь
    RENTAL_PERIOD = By.XPATH, "//div[@class='Dropdown-root']"  # Поле срока аренды
    RENTAL_PERIOD_DROPDOWN = By.XPATH, "//div[@class='Dropdown-menu']"  # Периоды
    LOCATOR_ONE_DAY = By.XPATH, "//div[contains(@class, 'Dropdown-option') and (text()='сутки')]"  # День
    LOCATOR_TWO_DAY = By.XPATH, "//div[contains(@class, 'Dropdown-option') and (text()='двое суток')]"  # Два дня
    LOCATOR_BLACK_CHECKBOX = By.ID, "black"  # Черный цвет
    LOCATOR_GREY_CHECKBOX = By.ID, "grey"  # Серый цвет
    LOCATOR_COMMENT = By.XPATH, "//input[@placeholder='Комментарий для курьера']"  # Поле комментария
    ORDER_BUTTON = By.XPATH, "//div[contains(@class, 'Order_Buttons')]//button[text()='Заказать']"  # Кнопка "Заказать"

    LOCATOR_CONFIRM = By.XPATH, "//div[text()='Хотите оформить заказ?']"  # Диалог подтверрждения
    YES_BUTTON = By.XPATH, "//button[text()='Да']"  #Кнопка "Да"
    ORDER_COMPLETED = By.XPATH, "//div[contains(@class, 'Order_ModalHeader')]"  #Информация о заказе
    ORDER_STATUS_BUTTON = By.XPATH, "//button[text()='Посмотреть статус']"  #Кнопка "Посмотреть статус"
    INCORRECT_FIRST_NAME_MESSAGE = [By.XPATH, ".//input[contains(@placeholder,'Имя')]/parent::div/div"]  #Текст ошибки неправильного имени
    INCORRECT_LAST_NAME_MESSAGE = [By.XPATH, ".//input[contains(@placeholder,'Фамилия')]/parent::div/div"]   #Текст ошибки неправильной фамилии
    INCORRECT_ADDRESS_MESSAGE = [By.XPATH, ".//input[contains(@placeholder,'Адрес')]/parent::div/div"]   #Текст ошибки адреса
    INCORRECT_PHONENUMBER_MESSAGE = [By.XPATH, ".//input[contains(@placeholder,'Телефон')]/parent::div/div"]   #Текст ошибки номера телефона

