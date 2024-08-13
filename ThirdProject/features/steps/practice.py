from behave import step
import time
from time import sleep
from telnetlib import EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC


@step('I am navigating to ebay website')
def navigate_to_site(context):
    context.driver.get(context.url)


@step('I search for a {item_name}')
def search_item(context, item_name):
    search_bar = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.XPATH,"//input[@aria-label='Search for anything']")),"Search bar not found")
    search_bar.send_keys(item_name)

    search_button = context.driver.find_element(By.XPATH, "//input[@id='gh-btn']")
    search_button.click()
    time.sleep(2)


@step('I apply filter {subcategory} under the {category}')
def apply_filter(context, subcategory, category):
    filter_checkbox = context.driver.find_element(By.XPATH,f"//li[@class='x-refine__main__list '][.//div[@class='x-refine__item__title-container' and text()='{category}']]//input[@aria-label='{subcategory}']")
    filter_checkbox.click()
    time.sleep(2)


@step('I verify if the items displayed are related to {item_name}')
def check_items(context, item_name):
    list_of_items = context.driver.find_elements(By.XPATH, "//div[@class='s-item__title']//span[@role='heading']")
    issues = []
    for item in list_of_items:
        if item.text:
            if item_name.lower() not in item.text.lower():
                issues.append(f"The word {item_name} not in {item.text} and hence not related")

    if issues:
        for issue in issues:
            print(issue)


@step('I validate if the items displayed are {subcategory} under {category}')
def check_filtered_items(context, subcategory, category):
    list_items_displayed = context.driver.find_elements(By.XPATH, "//li[contains(@id,'item')]")
    main_window = context.driver.current_window_handle
    issues = []
    for item in list_items_displayed:
        all_label_texts = []
        all_values_texts = []
        item_title = item.find_element(By.XPATH, ".//span[@role='heading']").text
        product_url = item.find_element(By.XPATH, ".//a[@class='s-item__link']").get_attribute('href')

        context.driver.execute_script(f"window.open('{product_url}');")
        context.driver.switch_to.window(context.driver.window_handles[-1])

        all_values = context.driver.find_elements(By.XPATH, "//dd[@class='ux-labels-values__values']")
        all_labels = context.driver.find_elements(By.XPATH, "//dt[@class='ux-labels-values__labels']")

        for label in all_labels:
            all_label_texts.append(label.text)

        for value in all_values:
            all_values_texts.append(value.text)

        item_specifications = dict(zip(all_label_texts, all_values_texts))

        if category in item_specifications.keys():
            if subcategory != item_specifications[category]:
                issues.append(f"{item_title} doesn't have a subcategory as {subcategory} but has it as {item_specifications[category]}")

        context.driver.close()
        context.driver.switch_to.window(main_window)

    if issues:
        for issue in issues:
            print(issue)


@step('I click on the following navigation links and verify the titles')
def click_navigation_links(context):
    for row in context.table:
        nav_link_text = row['navlink']
        expected_title = row['pagetitle']
        navlink_element = context.driver.find_element(By.XPATH, f"//li[@class='gh-t gh-divider-l']/a[text()=' {nav_link_text}']")
        navlink_element.click()
        time.sleep(2)
        actual_title = context.driver.title
        print(expected_title)
        print(actual_title)
        assert expected_title == actual_title, "Titles don't match"


@step('I validate if the items displayed are related to {item_name} in the first {max_pages} pages')
def check_items_pages(context, item_name, max_pages):
    max_page_number = int(max_pages)
    current_page_number = 1
    issues = []

    while current_page_number < max_page_number:
        list_items = context.driver.find_elements(By.XPATH, "//div[@class='s-item__title'][.//span[@role='heading']]")
        print(len(list_items))
        for item in list_items:
            item_title = item.text
            if item_title:
                if item_name.lower() not in item_title.lower():
                    issues.append(f"The word {item_name} not in {item_title} and hence not related")

        next_button = context.driver.find_element(By.XPATH, "//a[@aria-label='Go to next search page']")
        next_button.click()
        time.sleep(2)
        current_page_number = current_page_number + 1
        time.sleep(2)

    if issues:
        for issue in issues:
            print(issue)



@step('I validate if the items displayed are related to {item_name} until {max_page} pages given i am on {landing_page} page')
def check_items_given_pages(context, item_name, max_page, landing_page):
    landing_page_xpath = f"//a[@class='pagination__item' and text()='{landing_page}']"
    landing_page_element = context.driver.find_element(By.XPATH, landing_page_xpath)
    landing_page_element.click()
    landing_page_number = int(landing_page)
    max_page_number = int(max_page)
    issues = []

    while landing_page_number <= max_page_number:
        list_items = context.driver.find_elements(By.XPATH, "//div[@class='s-item__title']//span[@role='heading']")
        for item in list_items:
            item_title = item.text
            if item_title:
                if item_name.lower() not in item_title.lower():
                    issues.append(f"The word {item_name} not in {item_title} and hence not related")

        next_button = context.driver.find_element(By.XPATH, "//a[@aria-label='Go to next search page']")
        next_button.click()
        time.sleep(5)

        landing_page_number = landing_page_number + 1

    if issues:
        for issue in issues:
            print(issue)


@step('I verify if the slider is visible')
def verify_slider_is_visible(context):
    WebDriverWait(context.driver,10).until(EC.presence_of_element_located((By.XPATH,"//ul[@class='carousel__list' and @id='s0-1-0-49-1-2-4-17[0[0]]-0[1]-2-@match-media-0-@ebay-carousel-list']")),"Slider not found")


@step('I click on Previous button and verify if its functional')
def previous_button_functionality(context):
    WebDriverWait(context.driver,10).until(EC.presence_of_element_located((By.XPATH,"//ul[@class='carousel__list' and @id='s0-1-0-49-1-2-4-17[0[0]]-0[1]-2-@match-media-0-@ebay-carousel-list']/li[1]")),"First Slide not found")
    previous_button = context.driver.find_element(By.XPATH, "//button[@aria-label='Go to previous banner']")
    previous_button.click()
    current_slide = context.driver.find_element(By.XPATH,"//ul[@class='carousel__list' and @id='s0-1-0-49-1-2-4-17[0[0]]-0[1]-2-@match-media-0-@ebay-carousel-list']//li[@class='carousel__snap-point vl-carousel__item' and not(@aria-hidden)]")
    last_slide = WebDriverWait(context.driver,10).until(EC.presence_of_element_located((By.XPATH,"//ul[@class='carousel__list' and @id='s0-1-0-49-1-2-4-17[0[0]]-0[1]-2-@match-media-0-@ebay-carousel-list']/li[4]")),"Fourth Slide not found")
    assert current_slide == last_slide, "Previous button not working as expected"
