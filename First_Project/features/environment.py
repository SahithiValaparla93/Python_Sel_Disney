import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def before_all(context):
    ...


def before_feature(context, feature):
    context.url = "https://www.ebay.com"


def before_scenario(context, scenario):
    context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))



def before_step(context, step):
    ...


def after_step(context, step):
    if step.status == 'failed':
        current_dir = os.path.dirname(__file__)
        rel_path_to_dest_folder = os.path.join(current_dir, 'failed_screenshots')
        if not os.path.exists(rel_path_to_dest_folder):
            os.makedirs(rel_path_to_dest_folder)
        context.driver.save_screenshot(os.path.join(rel_path_to_dest_folder, 'screenshot.png'))


def after_scenario(context, scenario):
    ...


def after_feature(context, feature):
    ...


def after_all(context):
    ...