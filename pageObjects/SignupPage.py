from appium.webdriver.common.appiumby import AppiumBy
from . import conftest

class SignupPage:
    tab_login_accid = 'Login'
    tab_signup_xpath = '//android.view.ViewGroup[@content-desc="button-sign-up-container"]/android.view.ViewGroup/android.widget.TextView'
    textbox_email_accid = 'input-email'
    textbox_password_accid = 'input-password'
    textbox_confirmpass_accid = 'input-repeat-password'
    button_submit_xpath = '//android.view.ViewGroup[@content-desc="button-SIGN UP"]/android.view.ViewGroup/android.widget.TextView'
    popup_success_xpath = '*//android.widget.TextView[@resource-id="android:id/message"]'

    def __init__(self):
        self.driver = conftest.getDriver()

    def gotoSignUp(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, self.tab_login_accid).click()
        self.driver.find_element(AppiumBy.XPATH, self.tab_signup_xpath).click()

    def insertEmail(self, email):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, self.textbox_email_accid).send_keys(email)

    def insertPassword(self, password):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, self.textbox_password_accid).send_keys(password)

    def insertConfPassword(self, confpassword):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, self.textbox_confirmpass_accid).send_keys(confpassword)

    def clickSignUP(self):
        self.driver.find_element(AppiumBy.XPATH, self.button_submit_xpath).click()

    def getStatus(self):
        self.driver.implicitly_wait(10)
        self.driver.save_screenshot("Screenshots/SignupSuccess.png")
        success = self.driver.find_element(AppiumBy.XPATH, self.popup_success_xpath).text
        return success
    #





