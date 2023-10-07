import time
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def browser():
    options = Options()
    # options.add_argument('--ignore-certificate-errors')
    # options.add_experimental_option('prefs', {'intl.accept_languages': getting_language})

    wb = webdriver.Chrome(options=options)
    # wb.implicitly_wait(3)
    yield wb
    time.sleep(3)
    wb.close()
