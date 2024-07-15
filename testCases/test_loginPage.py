from pageObjects.LoginPage import LoginPage
from utilities.customLogger import Logger

class Test_LoginPage:

    def test_login(self):
        Logger.log_info("***********************Login Test Start****************************")
        self.sup = LoginPage()
        self.sup.gotoSignUp()
        self.sup.insertEmail('test@tp.com')
        Logger.log_info("***********************Email Inserted****************************")
        self.sup.insertPassword('sup@1234')
        Logger.log_info("***********************Password Inserted****************************")
        self.sup.clickLogin()
        Logger.log_info("***********************Login Button Clicked****************************")
        success = self.sup.getStatus()
        if success == "You are logged in!":
            Logger.log_info("***********************Login Test Passed****************************")
            assert True
        else:
            Logger.log_info("***********************Login Test Failed****************************")
            assert False
        Logger.log_info("***********************Login Test End****************************")

NodeJS-WebdriverIO-Web
NodeJS-WebdriverIO-Web
NodeJS-WebdriverIO-Mobile
NodeJS-NightwatchJS-Web
NodeJS-NightwatchJS-Mobile
NodeJS-Puppeteer-Web
NodeJS-TestCafe-Web
NodeJS-Protractor-Web
NodeJS-Cypress-Web
NodeJS-Cypress-API
NodeJS-Axios-API
NodeJS-Playwright-Web
TypeScript-WebdriverIO-Web
TypeScript-WebdriverIO-Mobile
TypeScript-NightwatchJS-Web
TypeScript-NightwatchJS-Mobile
TypeScript-Puppeteer-Web
TypeScript-TestCafe-Web
TypeScript-Protractor-Web
Java-SeleniumWebDriver-Web
Java-SeleniumWebDriver-Mobile
Java-Appium-Mobile
Java-JUnit-Web
Java-RestAssured-API
Java-TestNG-Web
Java-Cucumber-Web
Java-Serenity-Web
Java-Selenide-Web
Java-Playwright-Web
Python-SeleniumWebDriver-Web
Python-Pylenium-Mobile
Python-RobotFramework-Web
Python-Behave-Web
Python-Playwright-Web
Python-Pytest-API