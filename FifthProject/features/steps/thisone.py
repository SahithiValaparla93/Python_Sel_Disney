from behave import step
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@step('I navigate to the ebay website')
def navigation(context):
    context.driver.get(context.url)
