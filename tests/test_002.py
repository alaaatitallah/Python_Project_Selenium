from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from Pages.LoginPage import LoginPage
import pytest
import os
class Test_002_Login:
    url = "https://admin-demo.nopcommerce.com/"
    username = "admin@yourstore.com"
    password = "admin"
    def test_homePageTitle(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        actualTitle = self.driver.title

        if actualTitle == "Your store. Login":
            self.driver.close()
            assert True
        else :
            self.driver.save_screenshot(".tests/screenshots/test_homePageTitle.png")
            self.driver.close()
            assert False
    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.loginPage = LoginPage(self.driver)
        #utilisation des methodes pour interagir avec la page
        self.loginPage.setUserName(self.username)
        self.loginPage.setPassword(self.password)
        self.loginPage.clickLogin()
        actualTitle = self.driver.title
        if actualTitle == "Dashboard / nopCommerce administration" :
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(":/tests/screenshots/" + "test_login.png")
            self.driver.close()
            assert False