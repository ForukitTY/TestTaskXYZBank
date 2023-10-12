import os
import allure

from main.pages.login_page import LoginPage
from main.pages.customer_login_page import CustomerLoginPage
from main.pages.account_page import AccountPage
from main.pages.transactions_page import TransactionsPage
from main.helpers.helper import solve_fibonacci_quiz, save_transactions_to_scv


class Steps:
    def __init__(self, browser):
        self.browser = browser

    @allure.step("Step 1. Go to customer login page")
    def step1_go_to_customer_login_page(self):
        login_page = LoginPage(self.browser)
        login_page.open()
        login_page.go_to_customer_login_page()

    @allure.step("Step 2. Login to account via user 'Harry Potter'")
    def step2_login_via_harry_potter(self):
        user_name = "Harry Potter"
        customer_login_page = CustomerLoginPage(self.browser)
        customer_login_page.choose_customer_by_name(name=user_name)
        customer_login_page.login_button().click()

    @allure.step("Step 3. Fill and debit from the account")
    def step3_amount_and_withdrawl_balance(self):
        account_page = AccountPage(self.browser)
        deposit_amount: int = solve_fibonacci_quiz()
        account_page.deposit_button().click()
        account_page.amount_input().send_keys(deposit_amount)
        account_page.submit_button().click()

        account_page.withdrawl_button().click()
        account_page.withdrawl_label()  # ждем пока обновиться лейбл над эдитом, иначе дублируется пополнение баланса
        account_page.amount_input().send_keys(deposit_amount)
        account_page.submit_button().click()

    @allure.step("Step 4. Check the balance. Need to be zero")
    def step4_check_balance(self):
        account_page = AccountPage(self.browser)
        assert account_page.get_balance == '0', (f"Неверный баланс после пополнения и списания.")

    @allure.step("Step 5. Go to transactions page")
    def step5_go_to_transactions_page(self):
        account_page = AccountPage(self.browser)
        account_page.transactions_button().click()

    @allure.step("Step 6. Check transactions history")
    def step6_check_transactions_history(self):
        listTx = TransactionsPage(self.browser)
        rows: list = listTx.get_table_rows()
        assert len(rows) == 2, f"Неверное количество транзакций в таблице из страницы {listTx.url}"

    @allure.step("Step 7. Save transactions to csv")
    def step7_save_transactions_csv(self):
        listTx = TransactionsPage(self.browser)
        rows_for_csv = listTx.get_table_rows_structured_list
        save_transactions_to_scv(rows_for_csv, path=os.path.dirname(__file__))


@allure.title("Check transactions history")
@allure.label("owner", "Gedgafov Mukhamed")
@allure.link("https://www.globalsqa.com/angularJs-protractor/BankingProject", name="XYZBank")
def test_transactions(browser, attach_transactions_csv):
    """
    Цель теста:
        1. Проверить что баланс при пополнении и списании одной и той же суммы = 0
        2. Проверить что транзакции есть в таблице транзакций
    """
    steps = Steps(browser)
    steps.step1_go_to_customer_login_page()
    steps.step2_login_via_harry_potter()
    steps.step3_amount_and_withdrawl_balance()
    steps.step4_check_balance()
    steps.step5_go_to_transactions_page()
    steps.step6_check_transactions_history()
    steps.step7_save_transactions_csv()
