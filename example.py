from explicit import waiter
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    driver.get("https://github.com/this/doesntexist")

    username_field = waiter.find_element(driver, "login_field", By.ID)
    username_field.click()
    username_field.send_keys("my_username")

    password_field = waiter.find_element(driver, "password", By.ID)
    password_field.click()
    password_field.send_keys("my_password")

    login_button = waiter.find_element(driver, "input.btn-primary", By.CSS_SELECTOR)
    login_button.click()
finally:
    driver.quit()


from explicit import waiter
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    driver.get("https://github.com/this/doesntexist")

    waiter.find_write(driver, "login_field", "my_username", by=By.ID)

    waiter.find_write(driver, "password", "my_password", by=By.ID, send_enter=True)

finally:
    driver.quit()
