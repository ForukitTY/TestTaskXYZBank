from selenium.webdriver.common.by import By


class BasePageLocators:

    HOME_BUTTON = (By.CSS_SELECTOR, "body > div > div > div.box.mainhdr > button.btn.home")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "body > div > div > div.box.mainhdr > button.btn.logout")


class LoginPageLocators:

    CUSTOMER_LOGIN_BUTTON = (By.CSS_SELECTOR, "body > div > div > div.ng-scope > div > div.borderM.box.padT20 > div:nth-child(1) > button")
    BANK_MANAGER_LOGIN_BUTTON = (By.CSS_SELECTOR, "body > div > div > div.ng-scope > div > div.borderM.box.padT20 > div:nth-child(3) > button")


class CustomerLoginPageLocators:

    YOUR_NAME_DROPLIST = (By.ID, "userSelect")
    YOUR_NAME_DROPLIST_ROWS = (By.TAG_NAME, "option")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "body > div > div > div.ng-scope > div > form > button")


class AccountPageLocators:

    TRANSACTIONS_BUTTON = (By.CSS_SELECTOR, "body > div > div > div.ng-scope > div > div:nth-child(5) > button:nth-child(1)")
    DEPOSIT_BUTTON = (By.CSS_SELECTOR, "body > div > div > div.ng-scope > div > div:nth-child(5) > button:nth-child(2)")
    WITHDRAWL_BUTTON = (By.CSS_SELECTOR, "body > div > div > div.ng-scope > div > div:nth-child(5) > button:nth-child(3)")
    WITHDRAWL_LABEL = (By.XPATH, "//*[@class='form-group']/label[contains(text(), 'Amount to be Withdrawn :')]")
    BALANCE = (By.CSS_SELECTOR, "body > div > div > div.ng-scope > div > div:nth-child(3) > strong:nth-child(2)")
    AMOUNT_INPUT = (By.XPATH, "//input[@type='number']")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "body > div > div > div.ng-scope > div > div.container-fluid.mainBox.ng-scope > div > form > button")


class TransactionsPageLocators:

    BACK_BUTTON = (By.CSS_SELECTOR, "body > div > div > div.ng-scope > div > div.fixedTopBox > button:nth-child(1)")
    RESET_BUTTON = (By.CSS_SELECTOR, "body > div > div > div.ng-scope > div > div.fixedTopBox > button:nth-child(3)")
    TABLE_BODY = (By.CSS_SELECTOR, "body > div > div > div.ng-scope > div > div:nth-child(2) > table > tbody")
    TABLE_HEADERS = (By.CSS_SELECTOR, "body > div > div > div.ng-scope > div > div:nth-child(2) > table > thead > tr > td")
    TABLE_ROWS = (By.XPATH, "//tbody/tr")


