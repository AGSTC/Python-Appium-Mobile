from pageObjects.HomePage import HomePage

class Test_HomePage:

    def test_homePage(self):
        self.hp = HomePage()

        self.title = self.hp.getTitle()
        if self.title == "WEBDRIVER":
            assert True
        else:
            assert False

        self.info = self.hp.getInfo()
        if self.info == "Demo app for the appium-boilerplate":
            assert True
        else:
            assert False

        self.support = self.hp.getSupport()
        if self.support == "Support":
            assert True
        else:
            assert False
