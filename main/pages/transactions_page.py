from typing import List, Dict

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

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

    def find_table_rows(self) -> List[WebElement]:
        try:  # использую try/except т.к в некоторый случаях таблица отображется пустой, до обновления страницы
            return self.find_elements(TransactionsPageLocators.TABLE_ROWS)
        except TimeoutException:
            self.browser.refresh()
            return self.find_elements(TransactionsPageLocators.TABLE_ROWS)

    @property
    def get_table_rows_structured_list(self) -> List[Dict]:
        """
        :return: List like  [{'Date-Time': 'Oct 9, 2023 3:34:42 PM', 'Amount': '34', 'Transaction Type': 'Debit'},...]
        """
        headers: List[WebElement] = self.find_elements(TransactionsPageLocators.TABLE_HEADERS)
        rows: List[WebElement] = self.find_table_rows()

        rows_list = []
        row_dict = {}
        for row in rows:
            cells: List[WebElement] = row.find_elements(By.TAG_NAME, "td")
            for column_name, cell in zip(headers, cells):
                row_dict[column_name.text] = cell.text
            rows_list.append(row_dict)

        return rows_list
