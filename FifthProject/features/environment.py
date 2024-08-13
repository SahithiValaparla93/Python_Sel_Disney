from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
import os


def after_all(context):
    ...


def before_all(context):
    ...


def before_scenario(context, scenario):
    context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


def after_scenario(context, scenario):
    ...


def after_step(context, step):
    if step.status == 'failed':
        current_dir = os.path.dirname(__file__)
        relative_path_to_dest = os.path.join(current_dir, 'failed_screenshots')
        if not os.path.exists(relative_path_to_dest):
            os.makedirs(relative_path_to_dest)
        context.driver.save_screenshot(os.path.join(relative_path_to_dest, step.name + '.png'))




def before_step(context, step):
    ...


def before_feature(context, feature):
    context.url = "https://eby.com/"


def after_feature(context, feature):
    ...