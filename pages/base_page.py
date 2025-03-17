from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException, NoSuchElementException

from conftest import driver


class BasePage:
    # Тут описываются локаторы
    waiting_time = 20
    LOGOUT_BUTTON = ("xpath", "//button[@id='logout']")
    LOGO_LINK = ("xpath", "//a[@id='logo']")
    ...

    # Тут создаются необходимые обьекты, которые будут доступны в pages
    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.wait = WebDriverWait(self.driver, timeout=self.waiting_time, poll_frequency=1)
        self.ec = EC
        self.select = Select

    # Данный метод будет вызываться для любой страницы, принимая ее PAGE_URL
    def open(self):
        self.driver.get(self.PAGE_URL)

    # Ниже описываются общие для всех страниц методы
    def click_on_logout_button(self):
        self.driver.find_element(*self.LOGOUT_BUTTON).click()

    def waite_visible_element(self, xpath_locator:str):
        """Ожидает видимый элемент"""
        return self.wait.until(self.ec.visibility_of_element_located(('xpath', xpath_locator)))

    def presence_of_element_located(self, xpath_locator:str):
        """Ожидает видимый элемент"""
        return self.wait.until(self.ec.presence_of_element_located(('xpath', xpath_locator)))

    def select_by_visible_text(self, select_xpath_locator:str, select_options_text:str):

        dropdown = self.waite_visible_element(select_xpath_locator)
        select = self.select(dropdown)
        self.scroll_in_too('xpath', select_xpath_locator)
        select.select_by_visible_text(select_options_text)


    def presence_by_locate_text(self, select_xpath_locator:str, select_options_text:str):
        dropdown = self.presence_of_element_located(select_xpath_locator)
        select = self.select(dropdown)
        select.select_by_visible_text(select_options_text)

    def select_calender_data(self, calender_data:str):
        locator = f'//a[@class="ui-state-default" and normalize-space(text())="{calender_data}"]'
        self.scroll_in_too('xpath', locator)
        self.waite_visible_element(xpath_locator=locator).click()

    def scroll_in_too(self, how, what):
        """Метод скролинга до элемента c проверкой видимости"""
        try:
            position = self.driver.find_element(how, what)
            self.driver.execute_script("return arguments[0].scrollIntoView();", position)
            WebDriverWait(self.driver, self.waiting_time).until(
                EC.visibility_of_element_located((how, what)))

        except (NoSuchElementException, TimeoutException):
            return False
        return True

