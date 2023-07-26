# Sprint_4
Тестирование учебного сервиса «Яндекс.Самокат»

1. Фреймворк selenium.
2. Браузер - Firefox
3. Команда для запуска всех тестов — pytest -v tests
4. Генерация отчетов Allure: pytest  --alluredir=allure_results
5. Для формирования отчета в формате веб-страницы: allure serve allure_results 

Описание тестов:
test_base_page.py - проверка перехода по логотипам
test_order.py - проверка страниц заказа
test_questions.py - проверка блока Вопросы о важном
