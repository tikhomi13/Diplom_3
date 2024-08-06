import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
import faker


class URLs:

    BASE_URL = 'https://stellarburgers.nomoreparties.site/'

    FEED_URL = f'{BASE_URL}feed'

    LK_URL = f'{BASE_URL}login'

    RECOVER_URL = f'{BASE_URL}forgot-password'




class ChromeData: # не уверен что нужно

    print(123)



class FirefoxData:

    print(123)


class WebDriverFactory:

    @staticmethod
    def getWebDriver(browserName):
        if browserName == 'firefox':
            return webdriver.Firefox()
        elif browserName == 'chrome':
            return webdriver.Chrome()

class FakeData:

    def fake_email(self):

        fake = faker.Faker()
        email = fake.email()

        return email



