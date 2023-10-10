import os
import time
import pytest
import allure

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def browser():
    options = Options()
    wb = webdriver.Chrome(options=options)
    # wb.implicitly_wait(3)
    yield wb
    screenshot_as_png = wb.get_screenshot_as_png()
    allure.attach(screenshot_as_png, name="full-page", attachment_type=allure.attachment_type.PNG)
    time.sleep(5)  # убрать в конечном варианте
    wb.close()


@pytest.fixture
def attach_transactions_csv():
    yield
    filename = "transactions.csv"

    if os.path.isfile(filename):
        allure.attach.file(filename, name=filename, attachment_type=allure.attachment_type.CSV)
        os.remove(filename)
