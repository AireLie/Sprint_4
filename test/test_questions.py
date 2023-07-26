import allure
import pytest
from pages.main_page import MainPage
from data import Questions
from url import Urls

@pytest.mark.usefixtures("driver")
class TestQuestions:

    @allure.title('Раздел "Вопросы о важном"')

    @pytest.mark.parametrize("index,text", Questions.QUESTIONS_LIST)

    def test_get_answer_on_question_FAQ_passed(self, driver, index, text):

        questions = MainPage(driver)
        questions.open_page(Urls.MAIN_PAGE)
        questions.scroll_to_questions()
        questions.click_on_question(index)
        answer = questions.get_answer_text()
        questions.wait_for_get_answer()

        assert answer == text