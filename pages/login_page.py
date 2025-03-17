from pages.base_page import BasePage
from faker import Faker



# Класс страницы
class LoginPage(BasePage):  # Наследование от BasePage

    fake = Faker()
    fake_email = fake.email()


    # URL страницы
    # PAGE_URL = "https://demo.opensource-socialnetwork.org/"
    PAGE_URL = "http://qa-playground-social.com/"

    # Локаторы страницы
    FIRST_NAME_FIELD = "//input[@placeholder='First Name']"
    LAST_NAME_FIELD = "//input[@placeholder='Last Name']"
    EMAIL_FIELD = "//input[@placeholder='Email']"
    RE_ENTER_EMAIL_FIELD = "//input[@placeholder='Re-enter Email']"
    USER_NAME_FIELD = "//input[@placeholder='Username']"
    PASSWORD_FIELD = "//input[@placeholder='Password']"
    MALE_RADIO_BUTTON = '(//input[@class="ossn-radio-input ossn-field-required"])[1]'
    CONFIRM_RADIO_BUTTON = '//input[@name="gdpr_agree"]'
    BIRTHDATE_OBJ = "//input[@placeholder='Birthdate']"

    LOGIN_BUTTON = ("xpath", "//input[@id='ossn-submit-button']")


    def enter_first_name(self):
        self.waite_visible_element(self.FIRST_NAME_FIELD).send_keys(self.fake.first_name())

    def enter_last_name(self):
        self.waite_visible_element(self.LAST_NAME_FIELD).send_keys(self.fake.last_name())

    def enter_email(self):
        self.waite_visible_element(self.EMAIL_FIELD).send_keys(self.fake_email)

    def enter_confirm_email(self):
        self.waite_visible_element(self.RE_ENTER_EMAIL_FIELD).send_keys(self.fake_email)

    def enter_username(self):
        self.waite_visible_element(self.USER_NAME_FIELD).send_keys(self.fake.user_name())

    def enter_password(self):
        self.waite_visible_element(self.PASSWORD_FIELD).send_keys(self.fake.password())

    def click_on_male_button(self):
        self.waite_visible_element(self.MALE_RADIO_BUTTON).click()

    def click_on_confirm_button(self):
        self.waite_visible_element(self.CONFIRM_RADIO_BUTTON).click()

    def click_on_birthdate_button_and_insert_data_year_month(self, select_calender_data = '26',
                                                             select_year:str = '1984',
                                                             select_month: str = 'July',
                                                             ):
        OBJ_KALENDER = '//div[@id="ui-datepicker-div"]'
        DROPDOWN_MONTH = '//select[@class="ui-datepicker-month"]'
        DROPDOWN_YEAR = '//select[@class="ui-datepicker-year"]'
        self.waite_visible_element(self.BIRTHDATE_OBJ).click()
        self.waite_visible_element(OBJ_KALENDER)
        self.select_by_visible_text(DROPDOWN_MONTH, select_options_text=select_month)
        self.select_by_visible_text(DROPDOWN_YEAR, select_options_text=select_year)
        self.select_calender_data(select_calender_data)


    def click_on_login_button(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

