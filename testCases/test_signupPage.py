from pageObjects.SignupPage import SignupPage
from utilities.customLogger import Logger

class Test_SignUpPage:

    def test_signup(self):
        Logger.log_info("***********************Signup Test Start****************************")
        self.sup = SignupPage()
        self.sup.gotoSignUp()
        self.sup.insertEmail('test@tp.com')
        Logger.log_info("***********************Email Inserted****************************")
        self.sup.insertPassword('sup@1234')
        Logger.log_info("***********************Password Inserted****************************")
        self.sup.insertConfPassword('sup@1234')
        Logger.log_info("***********************Confirm Password Inserted****************************")
        self.sup.clickSignUP()
        Logger.log_info("***********************Signup Button Clicked****************************")
        success = self.sup.getStatus()
        if success == "You successfully signed up!":
            Logger.log_info("***********************Signup Test Passed****************************")
            assert True
        else:
            Logger.log_info("***********************Signup Test Failed****************************")
            assert False

        Logger.log_info("***********************Signup Test End****************************")