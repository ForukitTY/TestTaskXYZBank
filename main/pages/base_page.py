from typing import List, Tuple

import selenium.webdriver.support.expected_conditions as EC

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:

    def __init__(self, browser, url="https://www.globalsqa.com/angularJs-protractor/BankingProject"):
        self.browser: WebDriver = browser
        self.url: str = url

    def open(self):
        self.browser.get(self.url)

    def find_element(self, locator: Tuple[str, str], ec_method=EC.presence_of_element_located,
                     timeout: float = 5) -> WebElement:

        wait = WebDriverWait(self.browser, timeout)
        wait.until(ec_method(locator), message=f"Not found element {locator}")
        return self.browser.find_element(*locator)

    def find_elements(self, locator: Tuple[str, str], ec_method=EC.presence_of_element_located,
                      timeout: float = 5) -> List[WebElement]:

        wait = WebDriverWait(self.browser, timeout)
        wait.until(ec_method(locator), message=f"Not found element {locator}")
        return self.browser.find_elements(*locator)

    def is_element_present(self, locator: Tuple[str, str]):
        """Check element existence via WebDriver"""
        try:
            self.browser.find_element(*locator)
            return True
        except NoSuchElementException:
            return False

    def is_not_element_present(self, locator: Tuple[str, str]):
        try:
            self.browser.find_element(*locator)
            return False
        except NoSuchElementException:
            return True
