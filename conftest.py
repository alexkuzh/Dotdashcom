import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver(request):

    # edit for you
    download_folder = "D:/Download/"

    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--log-level=DEBUG')
    options.add_argument('--start-maximized')
    options.add_argument('--download.default_directory='+download_folder)

    driver = webdriver.Chrome(chrome_options=options)
    try:
        yield driver
    finally:
        driver.close()
