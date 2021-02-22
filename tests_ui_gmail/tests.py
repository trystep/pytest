from selenium.webdriver import Remote
from pytest import fixture
import allure
from tests_ui_gmail.page_object_models.LoginPage import LoginPage
from tests_ui_gmail.parameterization.parametrs import Parameters


@allure.step("Открыть Gmail")
def open_gmail(webdriver):
    webdriver.get(Parameters.gmail_url())
    return LoginPage(webdriver)


@fixture
def remote_webdriver(request):
    wd = Remote(Parameters.webdriver_url(), desired_capabilities={
        'platform': Parameters.webdriver_platform(),
        'browserName': Parameters.webdriver_browser(),
        'version': Parameters.webdriver_version(),
    })
    request.addfinalizer(wd.close)
    return wd


@allure.step("Сообщение отправляется успешно")
def test_mail_send_success(remote_webdriver):
    main_page = open_gmail(remote_webdriver) \
        .login(Parameters.gmail_username(), Parameters.gmail_password())
    main_page \
        .open_write_message() \
        .fill_message(Parameters.gmail_message_to(), Parameters.gmail_message_subject(),
                      Parameters.gmail_message_body()) \
        .send_message()
    main_page.get_notification().check_message_send()


@allure.step("Ожидаемо падает тест при отправке сообщения на невалидный адрес получателя")
def test_mail_send_with_invalid_recipient_fail(remote_webdriver):
    invalid_recipient = "124567"

    main_page = open_gmail(remote_webdriver) \
        .login(Parameters.gmail_username(), Parameters.gmail_password())

    main_page \
        .open_write_message() \
        .fill_message(invalid_recipient, Parameters.gmail_message_subject(), Parameters.gmail_message_body()) \
        .send_message()
    main_page.get_alert().check_error_message(
        "Адрес " + invalid_recipient + " в поле Кому не распознан. Проверьте правильность ввода всех адресов.")


@allure.step("Ожидаемо падает тест при отправке на пустой адрес получателя")
def test_mail_send_with_empty_recipient_fail(remote_webdriver):
    main_page = open_gmail(remote_webdriver) \
        .login(Parameters.gmail_username(), Parameters.gmail_password())

    main_page \
        .open_write_message() \
        .fill_message("", Parameters.gmail_message_subject(), Parameters.gmail_message_body()) \
        .send_message()
    main_page.get_alert().check_error_message("Укажите как минимум одного получателя.")
