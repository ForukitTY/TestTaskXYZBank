import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement

from main.pages.base_page import BasePage
from main.pages.locators import AccountPageLocators


class AccountPage(BasePage):
    def __init__(self, browser):
        url = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/account"
        super().__init__(browser, url)

    def transactions_button(self):
        button = self.find_element(AccountPageLocators.TRANSACTIONS_BUTTON)
        return button

    def deposit_button(self):
        button = self.find_element(AccountPageLocators.DEPOSIT_BUTTON)
        return button

    def withdrawl_button(self):
        button = self.find_element(AccountPageLocators.WITHDRAWL_BUTTON)
        return button

    def amount_input(self):
        edit = self.find_element(AccountPageLocators.AMOUNT_INPUT, ec_method=EC.element_to_be_clickable)
        return edit

    def withdrawl_label(self):
        label = self.find_element(AccountPageLocators.WITHDRAWL_LABEL)
        return label

    def submit_button(self):
        button = self.find_element(AccountPageLocators.SUBMIT_BUTTON)
        return button

    @property
    def get_balance(self) -> str:
        balance = self.find_element(AccountPageLocators.BALANCE)
        return balance.text
