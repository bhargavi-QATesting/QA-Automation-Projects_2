import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver

class Add_User_Page:

    link_admin_menu_xpath = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]'
    link_addnew_xpath = "//button[normalize-space()='Add']"
    link_userrole_xpath = "(//div[contains(@class,'oxd-select-text')])[1]"
    admin_option_xpath = "//div[@role='option']/span[text()='Admin']"
    ess_option_xpath = "//div[@role='option']/span[text()='ESS']"
    link_employeename_xpath = "//input[@placeholder='Type for hints...']"
    link_status_dropdown_xpath = "//div[contains(text(),'-- Select --')]"
    link_status_enabled_xpath = "//span[text()='Enabled']"
    link_username_xpath = "(//input[@class='oxd-input oxd-input--active'])[2]"
    link_password_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input'
    link_confirmpassword_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input'
    link_savebutton_xpath = "//button[normalize-space()='Save']"
    #link_search_button_xpath = "//button[normalize-space()='Search']"
    #link_search_username_xpath = "(//input[contains(@class,'oxd-input')])[2]"

    def __init__(self, driver):
        self.driver = driver

    def click_admin(self):
        self.driver.find_element(By.XPATH,self.link_admin_menu_xpath).click()

    def click_addnew(self):
        self.driver.find_element(By.XPATH,self.link_addnew_xpath).click()

    def click_userrole(self):
        self.driver.find_element(By.XPATH,self.link_userrole_xpath).click()
        #self.driver.find_element_by_xpath(self.link_userrolevalue_xpath).click()

    def click_admin_option_xpath(self):
        self.driver.find_element(By.XPATH,self.admin_option_xpath).click()

    def click_ess_option_xpath(self):
        self.driver.find_element(By.XPATH,self.ess_option_xpath).click()

    def click_employeename(self,empname):
        self.driver.find_element(By.XPATH,self.link_employeename_xpath).send_keys(empname)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//span[contains(text(),'{empname}')]")
            )
        ).click()
    def click_status(self):
       self.driver.find_element(By.XPATH, self.link_status_dropdown_xpath).click()
       self.driver.find_element(By.XPATH, self.link_status_enabled_xpath).click()

    def click_username(self,username):
        self.driver.find_element(By.XPATH,self.link_username_xpath).send_keys(username)

    def click_password(self,password):
        self.driver.find_element(By.XPATH,self.link_password_xpath).send_keys(password)

    def click_confirmpassword(self,cnfmpassword):
        self.driver.find_element(By.XPATH,self.link_confirmpassword_xpath).send_keys(cnfmpassword)

    def click_savebutton(self):
        self.driver.find_element(By.XPATH,self.link_savebutton_xpath).click()

    def click_searchbutton(self):
        self.driver.find_element(By.XPATH, self.link_search_button_xpath).click()

    def click_search_username(self,username):
        self.driver.find_element(By.XPATH, self.link_search_username_xpath).send_keys(username)



