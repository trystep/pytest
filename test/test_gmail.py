import allure
import pytest

from params.data import test_data


@pytest.mark.parametrize('letter', test_data, ids=[repr(x) for x in test_data])
@allure.feature('News')
def test_send_email(app, letter):
    with allure.step("Пишем письмо и отправляем"):
        app.write_letter(letter)
        app.go_to_sent_letters()

    with allure.step("Получаем список всех отправленных писем"):
        # Этот блок может не выполниться, т.к. данные на странице могут устареть.
        # Просто пробуем еще раз - это решает проблему.
        try:
            app.get_email_list()
            list_of_email = app.get_email_list()
        except:
            app.get_email_list()
            list_of_email = app.get_email_list()

    with allure.step("Проверяем, что наше письмо есть в списке отправленных"):
        assert letter.email_subject in list_of_email
