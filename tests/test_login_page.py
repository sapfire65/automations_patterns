import pytest
from pages.login_page import RegistrationPage
from time import sleep


class TestLoginPage:

    def setup_method(self):
        self.login_page = RegistrationPage(self.driver)  # Создаем обьект страницы

    # Вызываем через объект страницы все нужные методы, это и есть шаги теста
    def test_login_in_account(self):
        self.login_page.open()  # open() подхватит PAGE_URL именно с LoginPage
        self.login_page.enter_first_name()
        self.login_page.enter_last_name()
        self.login_page.enter_email()
        self.login_page.enter_confirm_email()
        self.login_page.enter_username()
        self.login_page.enter_password()
        self.login_page.click_on_male_button()
        self.login_page.click_on_confirm_button()
        self.login_page.click_on_birthdate_button_and_insert_data_year_month(
            '26', '2000', 'Sep.'
        )
        self.login_page.click_on_login_button()
        assert self.login_page.waite_message_done_registered()


        sleep(5)

