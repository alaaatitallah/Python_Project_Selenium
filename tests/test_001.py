from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from Pages.LoginPage import LoginPage
import pytest
from time import sleep
class Test_001_Login:
    url = "https://admin-demo.nopcommerce.com/"
    username = "admin@yourstore.com"
    password = "admin"
    def test_homePageTitle(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)
        actualTitle = self.driver.title
        assert actualTitle == "Your store. Login"
        self.driver.close()
        print("Test for home page passed")
    def test_login(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)
        #création de l'instance de LoginPage
        self.loginPage = LoginPage(self.driver)
        #utilisation des methodes pour interagir avec la page
        self.loginPage.setUserName(self.username)
        self.loginPage.setPassword(self.password)
        self.loginPage.clickLogin()
        sleep (8)
        actualTitle = self.driver.title
        assert actualTitle == "Dashboard / nopCommerce administration"