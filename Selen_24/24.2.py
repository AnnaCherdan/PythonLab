from selenium import webdriver
driver = webdriver.Firefox()
driver.get('https://google.com')
# driver.quit()


def test_search_example(driver):
    search_input = driver.find_element_by_name('q')
