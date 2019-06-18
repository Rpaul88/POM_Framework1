from pages.LoginPage import Login
from data.TestData import *

def test_login():
    lp=Login()
    lp.login_cms(USER_NAME,PASSWORD)

def test_logout():
    lp=Login()
    lp.logout_cms()








# from selenium import webdriver
# from selenium.webdriver import ActionChains
#
# driver=webdriver.Chrome(executable_path="C:/Users/Guest User/PycharmProjects/POM_Framework1/drivers/chromedriver.exe")
# driver.get("https://s1.demo.opensourcecms.com/wordpress/wp-login.php")
#
# # Login
# def test_login():
#
#     driver.find_element_by_id("user_login").send_keys("opensourcecms")
#     driver.find_element_by_id("user_pass").send_keys("opensourcecms")
#     driver.find_element_by_id("wp-submit").click()
#
# # Logout
# def test_logout():
#
#     act = ActionChains(driver)
#     act.move_to_element(driver.find_element_by_xpath("//img[@class='avatar avatar-26 photo']"))
#     act.perform()
#     driver.implicitly_wait(30)
#     driver.find_element_by_xpath("//a[text()='Log Out']").click()







