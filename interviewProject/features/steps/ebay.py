from telnetlib import EC
from behave import step
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support import expected_conditions as EC


@step('I navigate to ebay website')
def navigate(context):
    context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    context.driver.get('https://ebay.com')


@step('I apply the filter {subcategory} under {category}')
def apply_filter(context, subcategory, category):
    filter_checkbox = context.driver.find_element(By.XPATH, f"//li[@class='x-refine__main__list '][.//div[@class='x-refine__item__title-container' and text() = '{category}']]//input[@aria-label='{subcategory}']")
    filter_checkbox.click()


@step('I search for shoes')
def search_shoes(context):
    search_bar = context.driver.find_element(By.XPATH, "//input[@aria-label='Search for anything']")
    search_bar.send_keys('shoes')
    search_button = context.driver.find_element(By.XPATH, "//input[@id='gh-btn']")
    search_button.click()


@step('I verify if the title of the item matches the actual title')
def validate_items_displayed(context):
    main_window = context.driver.current_window_handle
    list_of_all_items = context.driver.find_elements(By.XPATH, "//li[contains(@id,'item')]")
    print(len(list_of_all_items))
    issues = []
    for item in list_of_all_items:
        expected_title = item.find_element(By.XPATH, ".//div[@class='s-item__title']").text
        expected_price = item.find_element(By.XPATH, ".//span[@class='s-item__price']").text
        product_url = item.find_element(By.XPATH, ".//a[@class='s-item__link']").get_attribute('href')
        context.driver.execute_script(f"window.open('{product_url}')")
        context.driver.switch_to.window(context.driver.window_handles[-1])
        actual_title_element = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h1[@class='x-item-title__mainTitle']//span")),"Title not found")
        actual_title = actual_title_element.text
        actual_price_element = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.XPATH,"//div[@class='x-price-primary']//span")),"Price not found")
        actual_price = actual_price_element.text
        if expected_title.lower().strip() != actual_title.lower().strip():
            issues.append(f"{actual_title} does not match with the {expected_title}")
        if actual_price.lower().strip() not in actual_price.lower().strip():
            issues.append(f"{actual_price} does not match with the {expected_price}")
        context.driver.close()
        context.driver.switch_to.window(main_window)

    if len(issues) > 0:
        for issue in issues:
            print(issue)