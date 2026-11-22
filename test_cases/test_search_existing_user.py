import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base_pages.Login_Admin_Page import Login_Admin_Page
from utilities.read_properties import Read_Config
from utilities.custom_logger import Log_Maker
import time
from base_pages.Search_User_Page import Search_User_Page

class Test_Search_Existing_User():
        admin_page_url = Read_Config.get_admin_page_url()
        username = Read_Config.get_username()
        password = Read_Config.get_password()
        logger = Log_Maker.log_gen()

        @pytest.mark.regression
        @pytest.mark.sanity
        def test_search_user_by_username(self,setup):
                self.logger.info("********Search user with username started**********")
                self.driver = setup
                self.driver.implicitly_wait(10)
                self.driver.get(self.admin_page_url)
                self.admin_lp = Login_Admin_Page(self.driver)
                self.admin_lp.enter_username(self.username)
                self.admin_lp.enter_password(self.password)
                self.admin_lp.click_login_button()
                self.driver.maximize_window()
                time.sleep(5)
                self.logger.info("************Login completed**********")
                time.sleep(5)
                self.logger.info("***********starting add customer test***********")
                self.search_user = Search_User_Page(self.driver)
                self.search_user.click_admin()
                # self.add_user.click_searchbutton()
                self.search_user.search_user_by_username("bhargavireddy")
                #self.search_user.click_emploee
                self.search_user.click_search_button()
                time.sleep(2)
                self.driver.save_screenshot(".\\screenshots\\test_search_customer.png")
                status = self.search_user.verify_username_present("bhargavireddy")

                if status:
                        self.logger.info("******** Test Passed ********")
                        assert True
                else:
                        self.driver.save_screenshot(".\\screenshots\\search_user_failed.png")
                        self.logger.info("******** Test Failed ********")
                        assert False

                self.driver.close()

        @pytest.mark.regression
        def test_search_user_by_employee_name(self, setup):
                self.logger.info("******** Search User By Employee Name Started ********")
                self.driver = setup
                self.driver.implicitly_wait(10)
                self.driver.get(self.admin_page_url)

                # Login
                self.admin_lp = Login_Admin_Page(self.driver)
                self.admin_lp.enter_username(self.username)
                self.admin_lp.enter_password(self.password)
                self.admin_lp.click_login_button()
                self.driver.maximize_window()
                time.sleep(5)

                self.logger.info("******** Login Successful ********")
                self.search_user = Search_User_Page(self.driver)
                self.search_user.click_admin()

                # Enter Employee Name
                self.search_user.search_user_by_employee_name("mQsUICmnRv Doe")
                self.search_user.click_search_button()
                time.sleep(3)

                self.driver.save_screenshot(".\\screenshots\\test_search_employee_name.png")
                status = self.search_user.verify_employee_name_present("mQsUICmnRv Doe")

                if status:
                        self.logger.info("******** Test Passed ********")
                        assert True
                else:
                        self.driver.save_screenshot(".\\screenshots\\search_employee_name_failed.png")
                        self.logger.info("******** Test Failed ********")
                        assert False

                self.driver.close()
