from main.pages.base_page import BasePage
from main.pages.locators import LoginPageLocators


class LoginPage(BasePage):
    def __init__(self, browser):
        url = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login"
        super().__init__(browser, url)

    def go_to_customer_login_page(self):
        link = self.find_element(LoginPageLocators.CUSTOMER_LOGIN_BUTTON)
        link.click()

    def go_to_manager_login_page(self):
        link = self.find_element(LoginPageLocators.BANK_MANAGER_LOGIN_BUTTON)
        link.click()
