from appium.webdriver.common.appiumby import AppiumBy
from . import conftest


class HomePage:
    text_title_xpath = '//android.widget.ScrollView[@content-desc="Home-screen"]/android.view.ViewGroup/android.widget.TextView[1]'
    text_info_xpath = '//android.widget.ScrollView[@content-desc="Home-screen"]/android.view.ViewGroup/android.widget.TextView[2]'
    text_support_xpath = '//android.widget.ScrollView[@content-desc="Home-screen"]/android.view.ViewGroup/android.widget.TextView[5]'

    def __init__(self):

        self.driver = conftest.getDriver()
        self.driver.implicitly_wait(10)

    def getTitle(self):
        title = self.driver.find_element(AppiumBy.XPATH, self.text_title_xpath).text
        return title

    def getInfo(self):
        info = self.driver.find_element(AppiumBy.XPATH, self.text_info_xpath).text
        return info
    
    def getSupport(self):
        support = self.driver.find_element(AppiumBy.XPATH, self.text_support_xpath).text
        return support


