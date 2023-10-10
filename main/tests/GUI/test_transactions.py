import os
import allure
import pytest

from main.pages.login_page import LoginPage
from main.pages.customer_login_page import CustomerLoginPage
from main.pages.account_page import AccountPage
from main.pages.transactions_page import TransactionsPage

from main.helpers.helper import solve_fibonacci_quiz, save_transactions_to_scv


@allure.step
def test_transactions(browser, attach_transactions_csv):
    """
    Цель теста:
        1. Проверить что баланс при пополнении и списании одной и той же суммы = 0
        2. Проверить что транзакции есть в таблице транзакций

    Test steps:
        Зайти на аккаунт под пользователем Harry Potter
        Выполнить пополнение счета на сумму n
        Выполнить списание со счета на сумму n
        Проверить (1)
        Перейти на страницу транзакций
        Проверить (2)
        Сохранить строки таблицы в файле transactions.csv
    """
    user_name = "Harry Potter"
    login_page = LoginPage(browser)
    login_page.open()
    login_page.go_to_customer_login_page()

    customer_login_page = CustomerLoginPage(browser)
    customer_login_page.choose_customer_by_name(name=user_name)
    customer_login_page.login_button().click()

    account_page = AccountPage(browser)
    deposit_amount = solve_fibonacci_quiz()
    account_page.deposit_button().click()
    account_page.amount_input().send_keys(deposit_amount)
    account_page.submit_button().click()

    account_page.withdrawl_button().click()
    account_page.withdrawl_label()
    account_page.amount_input().send_keys(deposit_amount)
    account_page.submit_button().click()
    assert account_page.get_balance == '0', (f"Неверный баланс у пользователя {user_name}, после пополнения и списания "
                                             f"суммы = {deposit_amount}")
    account_page.transactions_button().click()

    listTx = TransactionsPage(browser)
    rows = listTx.find_table_rows()
    assert len(rows) == 2, f"Неверное количество транзакций в таблице из страницы {listTx.url}"
    rows_for_csv = listTx.get_table_rows_structured_list

    save_transactions_to_scv(rows_for_csv, path=os.path.dirname(__file__))
