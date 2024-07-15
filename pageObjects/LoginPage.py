from appium.webdriver.common.appiumby import AppiumBy
from . import conftest

class LoginPage:
    tab_login_accid = 'Login'
    textbox_email_xpath = '//android.widget.EditText[@content-desc="input-email"]'
    textbox_password_accid = 'input-password'
    button_login_xpath = '//android.view.ViewGroup[@content-desc="button-LOGIN"]/android.view.ViewGroup'
    popup_success_xpath = '*//android.widget.TextView[@resource-id="android:id/message"]'

    def __init__(self):
        self.driver = conftest.getDriver()

    def gotoSignUp(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, self.tab_login_accid).click()

    def insertEmail(self, email):
        self.driver.find_element(AppiumBy.XPATH, self.textbox_email_xpath).send_keys(email)

    def insertPassword(self, password):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, self.textbox_password_accid).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(AppiumBy.XPATH, self.button_login_xpath).click()

    def getStatus(self):
        self.driver.implicitly_wait(10)
        success = self.driver.find_element(AppiumBy.XPATH,self.popup_success_xpath).text
        self.driver.save_screenshot("Screenshots/LoginSuccess.png")
        return success





