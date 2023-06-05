from driver_factory import webdriver_maker


if __name__ == '__main__':

    driver = webdriver_maker().create_webdriver()

    driver.get('https://ithelp.ithome.com.tw/articles/10299861')
