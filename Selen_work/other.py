from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pytest
import pathlib
from pathlib import Path
# from conf24 import driver
import time
import conf24


def test_search_example(driver):
    driver = webdriver.Firefox()
    driver.get('https://www.google.com/')

    time.sleep(5)

    search_input = driver.find_element_by_name('q')

    search_input.clear()
    search_input.send_keys('И тут я что-то печатаю')

    time.sleep(5)

    search_button = driver.find_element_by_name('btnK')
    search_button.submit()

    driver.save_screenshot('resault.png')


# driver.close()

# driver = webdriver.Firefox('D:\\Общие документы\\AnnCherdan\\Python\\geckodriver.exe')
# driver.get("http://www.python.org")

# path = Path("AnnCherdan", "Python", "geckodriver.exe")
dir_path = pathlib.Path.cwd()
path1 = Path(dir_path, "AnnCherdan", "Python", "geckodriver.exe")
print(path1)