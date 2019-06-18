from selenium import webdriver
from selenium.webdriver import ActionChains

driver=webdriver.Chrome(executable_path="C:/Users/Guest User/PycharmProjects/POM_Framework1/drivers/chromedriver.exe")
driver.get("https://s1.demo.opensourcecms.com/wordpress/wp-login.php")

class Login:

    # Login
    def login_cms(self,un,pwd):

        driver.find_element_by_id("user_login").send_keys(un)
        driver.find_element_by_id("user_pass").send_keys(pwd)
        driver.find_element_by_id("wp-submit").click()

    # Logout
    def logout_cms(self):

        act = ActionChains(driver)
        act.move_to_element(driver.find_element_by_xpath("//img[@class='avatar avatar-26 photo']"))
        act.perform()
        driver.implicitly_wait(30)
        driver.find_element_by_xpath("//a[text()='Log Out']").click()







