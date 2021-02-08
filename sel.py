from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("http://www.practiceselenium.com/")
elem = driver.find_element_by_class_name('editor_sidebarmore')
elem.click()
driver.implicitly_wait(5)
elem = driver.find_element_by_class_name('wsb-element-button')
elem.click()

driver.implicitly_wait(5)
elem = driver.find_element_by_id('email')
elem.send_keys("test@ing.com")

elem = driver.find_element_by_id('name')
elem.send_keys("Jane Doe")

elem = driver.find_element_by_id('address')
elem.send_keys("42 Walloby Street")

sel = Select(driver.find_element_by_id('card_type'))
sel.select_by_visible_text('Visa')

elem = driver.find_element_by_id('card_number')
elem.send_keys("123123123")

elem = driver.find_element_by_id('cardholder_name')
elem.send_keys("Jane Doe")

elem = driver.find_element_by_id('verification_code')
elem.send_keys("1111")


