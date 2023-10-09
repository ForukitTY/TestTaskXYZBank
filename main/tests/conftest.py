import time
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def browser():
    options = Options()
    wb = webdriver.Chrome(options=options)
    # wb.implicitly_wait(3)
    yield wb
    time.sleep(5)  # убрать в конечном варианте
    wb.close()

# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     ...