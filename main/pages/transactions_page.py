import selenium.webdriver.support.expected_conditions as EC
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By

from main.pages.base_page import BasePage
from main.pages.locators import TransactionsPageLocators


class TransactionsPage(BasePage):
    def __init__(self, browser):
        url = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/listTx"
        super().__init__(browser, url)

    def back_button(self):
        button = self.find_element(TransactionsPageLocators.BACK_BUTTON)
        return button

    def reset_button(self):
        button = self.find_element(TransactionsPageLocators.RESET_BUTTON)
        return button

    def find_table_rows(self):
        try:
            return self.find_elements(TransactionsPageLocators.TABLE_ROWS)
        except TimeoutException:
            self.browser.refresh()
            return self.find_elements(TransactionsPageLocators.TABLE_ROWS)

    @property
    def get_table_rows_structured_list(self):
        # # Вариант 1. Сухой текст
        # body = self.find_element(TransactionsPageLocators.TABLE_BODY)
        # return body.text.split("\n")

        # Вариант 2. Замудренно, но итог структурирован и далее может парсится в csv
        headers = self.find_elements(TransactionsPageLocators.TABLE_HEADERS)
        rows = self.find_table_rows()

        rows_list = []
        row_dict = {}
        for row in rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            for column_name, cell in zip(headers, cells):
                row_dict[column_name.text] = cell.text
            rows_list.append(row_dict)

        return rows_list
