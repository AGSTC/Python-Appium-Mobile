from appium import webdriver

def getDriver():
    desired_cap = {
      "appium:deviceName": "emulator-5554",
      "platformName": "Android",
      "appium:appPackage": "com.wdiodemoapp",
      "appium:appActivity": "com.wdiodemoapp.MainActivity"
        }

    driver = webdriver.Remote("http://localhost:4725/wd/hub", desired_cap)
    return driver
