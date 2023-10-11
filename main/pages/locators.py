from selenium.webdriver.common.by import By


class BasePageLocators:

    HOME_BUTTON = (By.XPATH, "//div[@class='box mainhdr']/button[contains(text(), 'Home')]")
    LOGOUT_BUTTON = (By.XPATH, "//div[@class='box mainhdr']/button[contains(text(), 'Logout')]")


class LoginPageLocators:

    CUSTOMER_LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Customer Login')]")
    BANK_MANAGER_LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Bank Manager Login')]")


class CustomerLoginPageLocators:

    YOUR_NAME_DROPLIST_ROWS = (By.XPATH, "//select[@id='userSelect']/option")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Login')]")


class AccountPageLocators:

    TRANSACTIONS_BUTTON = (By.XPATH, "//div[@class='center']/button[contains(text(),'Transactions')]")
    DEPOSIT_BUTTON = (By.XPATH, "//div[@class='center']/button[contains(text(),'Deposit')]")
    WITHDRAWL_BUTTON = (By.XPATH, "//div[@class='center']/button[contains(text(),'Withdrawl')]")
    WITHDRAWL_LABEL = (By.XPATH, "//*[@class='form-group']/label[contains(text(), 'Amount to be Withdrawn :')]")
    BALANCE = (By.XPATH, "//div[@class='center']/strong[2]")
    AMOUNT_INPUT = (By.XPATH, "//input[@type='number']")
    SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']")


class TransactionsPageLocators:

    BACK_BUTTON = (By.XPATH, "//div[@class='fixedTopBox']/button[contains(text(),'Back')]")
    RESET_BUTTON = (By.XPATH, "//div[@class='fixedTopBox']/button[contains(text(),'Reset')]")
    TABLE_BODY = (By.XPATH, "//table[@class='table table-bordered table-striped']/tbody")
    TABLE_HEADERS = (By.XPATH, "//table[@class='table table-bordered table-striped']/thead/tr/td")
    TABLE_ROWS = (By.XPATH, "//table[@class='table table-bordered table-striped']/tbody/tr")


