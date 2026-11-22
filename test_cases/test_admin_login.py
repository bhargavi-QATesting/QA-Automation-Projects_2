import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base_pages.Login_Admin_Page import Login_Admin_Page
from utilities.read_properties import Read_Config
from utilities.custom_logger import Log_Maker
import time

class TestAdminLogin:
    admin_page_url = Read_Config.get_admin_page_url()
    username = Read_Config.get_username()
    password = Read_Config.get_password()
    invalid_username = Read_Config.get_invalid_username()
    invalid_password = Read_Config.get_invalid_password()
    logger = Log_Maker.log_gen()

    @pytest.mark.regression
    def test_title_verification(self,setup):
        self.logger.info("************TestAdminLogin************")
        self.logger.info("************Verification of Title************")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(self.admin_page_url)

        act_title = self.driver.title
        exp_title = "OrangeHRM"
        if exp_title == act_title:
            self.logger.info("************Verification of Title title matched************")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_title_verification.png")
            self.logger.info("************Verification of Title title not matched************")
        # assert act_title == exp_title
            self.driver.close()
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_valid_admin_login(self,setup):
        self.logger.info("************test_valid_admin_login started************")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.admin_page_url)
        time.sleep(10)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login_button()
        time.sleep(5)
        act_page_text = self.driver.find_element(By.XPATH,"//h6[normalize-space()='Dashboard']").text
        if act_page_text == "Dashboard":
            self.logger.info("************Dashboard Text Found************")
            assert True
            self.driver.save_screenshot(".\\screenshots\\test_valid_admin_login.png")
            self.driver.close()
        else:
            self.driver.close()
            assert False
        #assert act_page_text == "Dashboard"
        #self.driver.quit()

    @pytest.mark.regression
    def test_invalid_admin_login(self,setup):
        self.logger.info("************test_invalid_admin_login started************")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.admin_page_url)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "username"))
        )
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.invalid_username)
        self.admin_lp.enter_password(self.invalid_password)
        time.sleep(5)
        self.admin_lp.click_login_button()
        time.sleep(5)
        error_msg = self.driver.find_element(By.XPATH,"//p[contains(@class,'oxd-alert-content-text')]").text
        if error_msg == "Invalid credentials":
            self.logger.info("************test_invalid_admin_login error message matched************")
            assert True
            self.driver.save_screenshot(".\\screenshots\\test_invalid_admin_login.png")
            self.driver.close()
        else:
            self.driver.close()
            assert False
        #assert error_msg == "Invalid credentials"
        #self.driver.quit()