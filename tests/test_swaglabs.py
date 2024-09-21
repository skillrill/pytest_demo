from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

print('Hello, World'!)
def login(username, password):
    if username != None: driver.find_element(By.ID, 'user-name').send_keys(username)
    if password != None: driver.find_element(By.NAME, 'password').send_keys(password)
    driver.find_element(By.CLASS_NAME, 'submit-button').click()

login_form_parameters = [
    ('standard_user', 'secret_sauce', 'products'),
    ('', '', 'Username is required'),
    ('problem_user', 'secret_sauce', 'products'),
    ('locked_out_user', 'secret_sauce', 'Sorry, this user has been locked out'),
    ('test', 'test', 'Username and password do not match any user in this service'),
]

@pytest.mark.parametrize("username, password, checkpoint", login_form_parameters)
def test_login(username, password, checkpoint):
    global driver
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get('https://www.saucedemo.com/')
    login(username, password)
    assert checkpoint.lower() in driver.page_source.lower()
    driver.quit()

@pytest.mark.smoke
def test_add_item_to_cart():
    global driver
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get('https://www.saucedemo.com/')
    login('standard_user', 'secret_sauce')
    add_to_cart_buttons = driver.find_elements(By.CLASS_NAME, 'btn_primary')
    add_to_cart_buttons[0].click()
    shopping_cart_icon = driver.find_element(By.CLASS_NAME, 'shopping_cart_badge')
    assert shopping_cart_icon.text == '1'
