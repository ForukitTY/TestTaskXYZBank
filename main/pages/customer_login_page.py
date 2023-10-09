from selenium.common import NoSuchElementException

from main.pages.base_page import BasePage
from main.pages.locators import CustomerLoginPageLocators


class CustomerLoginPage(BasePage):
    def __init__(self, browser):
        url = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/customer"
        super().__init__(browser, url)

    def choose_customer_by_name(self, name):
        """
        Open drop list and select row with name = {name}
        """
        drop_list = self.find_element(CustomerLoginPageLocators.YOUR_NAME_DROPLIST)
        rows = drop_list.find_elements(*CustomerLoginPageLocators.YOUR_NAME_DROPLIST_ROWS)
        for row in rows:
            if row.text == name:
                row.click()
                return
        raise NoSuchElementException(f"No such name as {name} in droplist on page {self.url}")

    def login_button(self):
        lb = self.find_element(CustomerLoginPageLocators.LOGIN_BUTTON)
        return lb
