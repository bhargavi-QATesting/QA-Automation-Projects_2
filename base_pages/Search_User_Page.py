import string
import time
from selenium.webdriver.common.by import By


class Search_User_Page:
    admin_menu_xpath = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]'
    search_username_xpath = "(//input[@class='oxd-input oxd-input--active'])[2]"
    search_button_xpath = "//button[normalize-space()='Search']"
    employeename_xpath = "//input[@placeholder='Type for hints...']"

    rowcount_xpath = "//div[@class='oxd-table-body']/div[@class='oxd-table-card']"
    username_colcount_xpath = "//div[@role='table']//div[@role='row']/div[2]"

    def __init__(self,driver):
        self.driver = driver

    def click_admin(self):
        self.driver.find_element(By.XPATH,self.admin_menu_xpath).click()

    def search_user_by_username(self, username):
        username_field = self.driver.find_element(By.XPATH,self.search_username_xpath)
        username_field.clear()
        username_field.send_keys(username)

    #def search_user_by_employeename(self, username):
        #self.driver.find_element(By.XPATH, self.search_username_xpath).send_keys(username)

    def click_search_button(self):
        self.driver.find_element(By.XPATH, self.search_button_xpath).click()

    def click_search_username(self, username):
        self.driver.find_element(By.XPATH,self.search_username_xpath).send_keys(username)

    def get_results_table_rows(self):
        return len(self.driver.find_elements(By.XPATH, self.rowcount_xpath))

    def get_results_table_cols(self):
        return len(self.driver.find_elements(By.XPATH, self.username_colcount_xpath))

    def verify_username_present(self, username):
        rows = self.driver.find_elements(By.XPATH,"//div[@class='oxd-table-body']//div[@role='row']")

        for row in rows:
            print(row.text)
            if username.lower() in row.text.lower():
                return True
        return False

    def search_user_by_employee_name(self, employee_name):
        emp = self.driver.find_element(By.XPATH,self.employeename_xpath)
        emp.clear()
        emp.send_keys(employee_name)
        time.sleep(2)
        try:
            self.driver.find_element(By.XPATH,"//div[@role='option']").click()
        except:
            pass

    def verify_employee_name_present(self, employee_name):
        rows = self.driver.find_elements(By.XPATH,"//div[@class='oxd-table-body']//div[@role='row']")

        for row in rows:
            print("ROW:", row.text)
            if employee_name.lower() in row.text.lower():
                return True
        return False

    '''def search_user_by_employeename(self, employeename):
        username_present_flag = False
        for r in range(1,self.get_results_table_rows+1):
            cus_username = self.driver.find_element(By.XPATH, self.username_colcount_xpath+str(r)).text

            if cus_username == employeename:
                username_present_flag = True
                break
        return username_present_flag'''




