#Locators and Action Methods
from selenium.webdriver.common.by import By


class Login_Admin_Page:
    textbox_username_name = "username"
    textbox_password_name = "password"
    button_login_xpath = "//button[@type='submit']"
    user_dropdown_xpath = "//span[@class='oxd-userdropdown-tab']"
    button_logout_xpath = "//a[normalize-space()='Logout']"

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(By.NAME, self.textbox_username_name).clear()
        self.driver.find_element(By.NAME, self.textbox_username_name).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.NAME, self.textbox_password_name).clear()
        self.driver.find_element(By.NAME, self.textbox_password_name).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def click_profile_dropdown(self):
        self.driver.find_element(By.XPATH,self.user_dropdown_xpath).click()

    def click_logout_button(self):
        self.driver.find_element(By.XPATH, self.button_logout_xpath).click()

