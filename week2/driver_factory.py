from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class webdriver_maker:

    def create_webdriver(self):

        option = self.create_option()

        PATH = 'C:/Users/User/OneDrive/桌面/webdriver/chromedriver.exe'

        driver = webdriver.Chrome(PATH, options=option)

        return driver

    @staticmethod
    def create_option():

        option = Options()

        option.add_experimental_option('detach', True)

        return option
