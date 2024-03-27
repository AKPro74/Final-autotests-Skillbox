
import pytest
from selenium import webdriver
import logging
from selenium.webdriver.chrome.options import Options

file_log = logging.FileHandler('Log.txt')
console_out = logging.StreamHandler()

logging.basicConfig(handlers=(file_log, console_out),
                    format='[%(asctime)s] %(levelname)s - Log.txt: %(message)s',
                    level=logging.INFO)  # '%m.%d.%Y %H:%M:%S',


# @pytest.fixture
# def browser():
#     logging.info('Запуск браузера')
#     chrome_browser = webdriver.Chrome()
#     chrome_browser.implicitly_wait(5)
#     chrome_browser.maximize_window()
#     return chrome_browser
