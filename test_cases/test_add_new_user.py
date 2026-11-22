import string
import time
import random

import pytest
from jinja2.compiler import generate
from selenium import webdriver
from selenium.webdriver.common.by import By
from base_pages.Login_Admin_Page import Login_Admin_Page
from utilities.read_properties import Read_Config
from utilities.custom_logger import Log_Maker
from base_pages.Add_User_Page import Add_User_Page

class Test_Add_New_User:
    admin_page_url = Read_Config.get_admin_page_url()
    username = Read_Config.get_username()
    password = Read_Config.get_password()
    logger = Log_Maker.log_gen()

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_add_new_user(self,setup):
        self.logger.info("************New Customer started**********")
        self.driver = setup
        self.driver.implicitly_wait(20)
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login_button()
        self.driver.maximize_window()
        self.logger.info("************Login completed**********")
        time.sleep(5)
        self.logger.info("***********starting add customer test***********")
        self.add_user = Add_User_Page(self.driver)
        self.add_user.click_admin()
        self.add_user.click_addnew()
        self.logger.info("***********Add new user test***********")
        self.add_user.click_userrole()
        self.add_user.click_admin_option_xpath()
        self.add_user.click_employeename("James  Butler")
        self.add_user.click_status()
        self.add_user.click_username("BhargaviReddy")
        self.add_user.click_password("Bhargavi@321")
        self.add_user.click_confirmpassword("Bhargavi@321")
        self.add_user.click_savebutton()
        self.driver.save_screenshot(".\\screenshots\\test_add_new_customer.png")
        time.sleep(2)
        self.driver.close()

    @pytest.mark.sanity
    def test_search_created_user(self,setup):
        self.logger.info("************New Customer started**********")
        self.driver = setup
        self.driver.implicitly_wait(20)
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login_button()
        self.driver.maximize_window()
        self.logger.info("************Login completed**********")
        time.sleep(5)
        self.logger.info("***********starting add customer test***********")
        self.add_user = Add_User_Page(self.driver)
        self.add_user.click_admin()
        #self.add_user.click_searchbutton()
        self.add_user.click_search_username("Bhargavi")
        self.add_user.click_searchbutton()
        time.sleep(2)
        self.driver.save_screenshot(".\\screenshots\\test_search_customer.png")






