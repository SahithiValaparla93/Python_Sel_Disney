import os

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService


def before_all(context):
    ...


def after_all(context):
    ...


def before_feature(context, feature):
    context.url ="https://ebay.com/"


def after_feature(context, feature):
    ...


def before_scenario(context, scenario):
    context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


def after_scenario(context, scenario):
    ...


def before_step(context, step):
    ...


def after_step(context, step):
    if step.status == 'failed':
        current_dir = os.path.dirname(__file__)
        path_to_dest_folder = os.path.join(current_dir, 'failed_screenshots')
        if not os.path.exists(path_to_dest_folder):
            os.makedirs(path_to_dest_folder)
        context.driver.save_screenshot(os.path.join(path_to_dest_folder, 'screenshot.png'))
