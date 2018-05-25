# encoding: utf-8
# a fast useful util of chrome driver
# the first time run this util may takes a few time of download chrome driver
# the detail document for this util please check the github


__version__ = '0.0.1'

from .web_driver.webdriver import WebDriver as webdriver

from .web_driver.webdriver_headless import WebDriverHeadless as webdriver_headless
