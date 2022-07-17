import pytest
from selenium import webdriver


@pytest.fixture
def firefox_options(firefox_options):
    firefox_options.binary = 'C:\\Program Files (x86)\\Mozilla Firefox\\Application'
    firefox_options.add_argument('-foreground')
    firefox_options.set_preference('browser.anchor_color', '#FF0000')
    return firefox_options


@pytest.fixture(scope="class")
def driver(request):
    driver = webdriver.Firefox("D:\\AllDoc\\AnnCherdan\\Python\\PtojectsPyCharm\\"
                               "PythonLab\\Selen_work\\geckodriver.exe")
