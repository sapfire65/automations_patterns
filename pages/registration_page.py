from pages.base_page import BasePage
from faker import Faker



# Класс страницы
class RegistrationPage(BasePage):  # Наследование от BasePage

    fake = Faker('ru_RU')
    fake_email = fake.email()



    # URL страницы
    # PAGE_URL = "https://demo.opensource-socialnetwork.org/"
    _PAGE_URL = "http://qa-playground-social.com/"

    # Локаторы страницы
    _FIRST_NAME_FIELD = "//input[@placeholder='First Name']"
    _LAST_NAME_FIELD = "//input[@placeholder='Last Name']"
    _EMAIL_FIELD = "//input[@placeholder='Email']"
    _TELEPHONE_FIELD = "//INPUT[@class='ossn-text-input mobilelogin']"
    _RE_ENTER_EMAIL_FIELD = "//input[@placeholder='Re-enter Email']"
    _USER_NAME_FIELD = "//input[@placeholder='Username']"
    _PASSWORD_FIELD = "//input[@placeholder='Password']"
    _MALE_RADIO_BUTTON = '(//input[@class="ossn-radio-input ossn-field-required"])[1]'
    _CONFIRM_RADIO_BUTTON = '//input[@name="gdpr_agree"]'
    _BIRTHDATE_OBJ = "//input[@placeholder='Birthdate']"
    _LOGIN_BUTTON = "//input[@id='ossn-submit-button']"
    _MESSAGE_DONE = "//div[@class='ossn-message-done']"


    def enter_first_name(self):
        self.waite_visible_element(self._FIRST_NAME_FIELD).send_keys(self.fake.first_name())

    def enter_last_name(self):
        self.waite_visible_element(self._LAST_NAME_FIELD).send_keys(self.fake.last_name())

    def enter_email(self):
        self.waite_visible_element(self._EMAIL_FIELD).send_keys(self.fake_email)

    def enter_telephone(self):
        self.waite_visible_element(self._TELEPHONE_FIELD).send_keys(self.fake.mobile_number())

    def enter_confirm_email(self):
        self.waite_visible_element(self._RE_ENTER_EMAIL_FIELD).send_keys(self.fake_email)

    def enter_username(self):
        self.waite_visible_element(self._USER_NAME_FIELD).send_keys(self.fake.user_name())

    def enter_password(self):
        self.waite_visible_element(self._PASSWORD_FIELD).send_keys(self.fake.password())

    def click_on_male_button(self):
        self.waite_visible_element(self._MALE_RADIO_BUTTON).click()

    def click_on_confirm_button(self):
        self.waite_visible_element(self._CONFIRM_RADIO_BUTTON).click()

    def click_on_birthdate_button_and_insert_data_year_month(self, select_calender_data = '26',
                                                             select_year:str = '1984',
                                                             select_month: str = 'July',
                                                             ):
        OBJ_KALENDER = '//div[@id="ui-datepicker-div"]'
        DROPDOWN_MONTH = '//select[@class="ui-datepicker-month"]'
        DROPDOWN_YEAR = '//select[@class="ui-datepicker-year"]'
        self.waite_visible_element(self._BIRTHDATE_OBJ).click()
        self.waite_visible_element(OBJ_KALENDER)
        self.select_by_visible_text(DROPDOWN_MONTH, select_options_text=select_month)
        self.select_by_visible_text(DROPDOWN_YEAR, select_options_text=select_year)
        self.select_calender_data(select_calender_data)


    def click_on_login_button(self):
        self.waite_visible_element(self._LOGIN_BUTTON).click()

    def waite_message_done_registered(self):
        return self.waite_visible_element(self._MESSAGE_DONE)


