import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


def before_all(context):
    ...


def after_all(context):
    ...


def before_feature(context, feature):
    context.url = "https://www.ebay.com"


def after_feature(context, feature):
    ...


def before_step(context, step):
    ...


def after_step(context, step):
    if step.status == 'failed':
        current_dir = os.path.dirname(__file__)  # where this file located
        relative_path_to_dest = os.path.abspath(os.path.join(current_dir, 'failed_screenshots'))
        if not os.path.exists(relative_path_to_dest):
            os.makedirs(relative_path_to_dest)
        context.driver.save_screenshot(os.path.join(relative_path_to_dest, f'{step.name}.png'))


def before_scenario(context, scenario):
    context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


def after_scenario(context, scenario):
    ...