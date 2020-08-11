from selenium import webdriver
import random
import time

#SING UP ----------------------------------------------------------------------------------------
def test_sign_up_conduit():
    driver = webdriver.Chrome()
    driver.get("https://react-redux.realworld.io/#/register?_k=mr2svn")
    driver.find_element_by_css_selector('[type="text"]').send_keys('test' + str(random.randint(0, 69696969)))
    driver.find_element_by_css_selector('[type="email"]').send_keys(str(random.randint(0, 69696969)) + '@gmail.com')
    driver.find_element_by_css_selector('[type="password"]').send_keys(str(random.randint(12345678, 87654321)))
    driver.find_element_by_css_selector('[type="submit"]').click()
    time.sleep(2)
    assert driver.find_element_by_css_selector('[href="#settings"]')
    driver.quit()
test_sign_up_conduit()

# SING IN ----------------------------------------------------------------------------------------
def test_login_conduit(driver):
    driver.get("https://react-redux.realworld.io/#/login?_k=tclgpm")
    driver.find_element_by_css_selector('[type="email"]').send_keys('enixan25@gmail.com')
    driver.find_element_by_css_selector('[type="password"]').send_keys('Enixan25')
    driver.find_element_by_css_selector('[type="submit"]').click()
    time.sleep(2)
    assert driver.find_element_by_css_selector('[href="#@enixan25"]')

# NEW POST ----------------------------------------------------------------------------------------
def test_new_post():
    driver = webdriver.Chrome()
    test_login_conduit(driver)
    driver.find_element_by_css_selector('[href="#editor"]').click()
    driver.find_element_by_css_selector('[placeholder="Article Title"]').send_keys('Test Article')
    driver.find_element_by_css_selector('[placeholder*="article about?"]').send_keys('test info')
    driver.find_element_by_css_selector('[placeholder*="(in markdown)"]').send_keys('Bla-Bla-Bla')
    driver.find_element_by_css_selector('[type="button"]').click()
    time.sleep(2)
    assert driver.find_element_by_xpath("//h1[contains(., 'Test Article')]")
    driver.quit()
test_new_post()