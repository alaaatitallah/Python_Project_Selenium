import pytest  
from selenium import webdriver 
from Pages.LoginPage import LoginPage  
from utilities.readProperties import ReadConfig  
from utilities.newCustomLogger import LogGen 


class Test_003_Login:
    """
    Classe de test pour vérifier la fonctionnalité de connexion.
    """

    # Lecture des configurations depuis le fichier de configuration
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    # Initialisation du logger pour enregistrer les logs des tests
    logger = LogGen("./Logs/automation.log")
    #logger = LogGen.loggen()  # Initialisation alternative commentée du logger

    def test_homePageTitle(self, setup):
        """
        Test pour vérifier le titre de la page d'accueil.

        Args:
            setup: Fixture Pytest pour initialiser le navigateur WebDriver.
        """
        self.logger.log_info("*************** Test_001_Login *****************")
        self.logger.log_info("****Started Home page title test ****")
        self.driver = setup
        self.logger.log_info("****Opening URL****")
        self.driver.get(self.baseUrl)
        act_title = self.driver.title

        if act_title == "Your store. Login":
            self.logger.log_info("**** Home page title test passed ****")
            self.driver.close()
            assert True
        else:
            self.logger.log_error("**** Home page title test failed****")
            self.driver.save_screenshot("./tests/Screenshots/" + "test_homePageTitle.png")
            self.driver.close()
            assert False

    def test_login(self, setup):
        """
        Test pour vérifier la fonctionnalité de connexion.

        Args:
            setup: Fixture Pytest pour initialiser le navigateur WebDriver.
        """
        self.logger.log_info("****Started Login Test****")
        self.driver = setup
        self.driver.get(self.baseUrl)
        
        # Création d'une instance de LoginPage pour interagir avec les éléments de la page de connexion
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        
        if act_title == "Dashboard / nopCommerce administration":
            self.logger.log_info("****Login test passed ****")
            self.driver.close()
            assert True
        else:
            self.logger.log_error("****Login test failed ****")
            self.driver.save_screenshot("./tests/Screenshots/" + "test_login.png")
            self.driver.close()
            assert False
