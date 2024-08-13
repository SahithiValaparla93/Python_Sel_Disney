from telnetlib import EC
from behave import step
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


@step('I am navigating to ebay website')
def navigate_to_website(context):
    context.driver.get(context.url)


@step('when I click on the below links')
def navigate_to_navigation_links(context):
    for row in context.table:
        link_text = row["Link Text"]
        link_element = context.driver.find_element(By.XPATH,f"//li[@class='gh-t gh-divider-l']/a[text()=' {link_text}']")
        link_element.click()

        time.sleep(2)

        actual_title = context.driver.title
        expected_title = row["Expected Title"]
        assert actual_title == expected_title, "Titles don't match, landed on a wrong page"


@step('I search for a {item_name}')
def search_dress(context, item_name):
    search_bar = WebDriverWait(context.driver,10).until(EC.presence_of_element_located((By.XPATH,"//input[@aria-label='Search for anything']")),"Element not found")
    search_bar.send_keys(item_name)
    search_button = context.driver.find_element(By.XPATH,"//input[@type='submit']")
    search_button.click()
    time.sleep(2)


@step('I verify if the items displayed are {item_name} related')
def verify_items_displayed(context, item_name):
    list_of_all_items = context.driver.find_elements(By.XPATH, "//div[@class='s-item__title']/span[@role='heading']")
    issues = []
    for item in list_of_all_items:
        item_title = item.text
        if item_title:
            if item_name.lower() not in item_title.lower():
                issues.append(f"{item_name} not in the {item_title} hence not related")

    if issues:
        for issue in issues:
            print(issue)


@step('I apply the filter {subcategory} under the {category}')
def apply_filter(context, subcategory, category):
    filter_checkbox = context.driver.find_element(By.XPATH, f"//li[@class='x-refine__main__list '][.//div[text()='{category}']]//input[@aria-label='{subcategory}']")
    filter_checkbox.click()


@step('I verify if the items are with {subcategory} under the {category}')
def verify_items(context, subcategory, category):
    issues = []
    main_window = context.driver.current_window_handle
    list_of_all_items = context.driver.find_elements(By.XPATH, "//li[contains(@id,'item')]")
    wait = WebDriverWait(context.driver, 10)
    print(len(list_of_all_items))
    for item in list_of_all_items:

        item_element = item.find_element(By.XPATH, ".//span[@role='heading']")
        item_title = item_element.text
        product_url = item.find_element(By.XPATH, ".//a[@class='s-item__link']").get_attribute("href")

        context.driver.execute_script(f"window.open('{product_url}')")
        context.driver.switch_to.window(context.driver.window_handles[-1])

        all_labels_list = context.driver.find_elements(By.XPATH, "//dt[@class='ux-labels-values__labels']")
        all_values_list = context.driver.find_elements(By.XPATH, "//dd[@class='ux-labels-values__values']")

        all_label_texts = []
        all_values_texts = []

        for label in all_labels_list:
            all_label_texts.append(label.text)

        for value in all_values_list:
            all_values_texts.append(value.text)

        item_specifications = dict(zip(all_label_texts, all_values_texts))

        if category in item_specifications.keys():
            print(category)
            print(item_specifications[category])
            if subcategory != item_specifications[category]:
                issues.append(f"{item_title} doesn't have a category as {subcategory}")
        else:
            print(f"{item_title} doesn't have a category as {category}")

        context.driver.close()
        context.driver.switch_to.window(main_window)

    if issues:
        for issue in issues:
            print(issue)


@step('I click on Shop By Category Dropdown')
def click_on_shop_by_category(context):
    shop_by_category = context.driver.find_element(By.XPATH, "//button[@id='gh-shop-a']")
    shop_by_category.click()


@step('I verify if the {heading} has the {expected_subheadings}')
def verify_subheadings(context, heading, expected_subheadings):
    actual_subheadings_elements_list = context.driver.find_elements(By.XPATH, f"//h3[@class='gh-sbc-parent'][.//a[text()='{heading}']]/following-sibling::ul[1]/li")
    actual_subheadings_list = []

    for element in actual_subheadings_elements_list:
        actual_subheadings_list.append(element.text)

    expected_subheadings_list = expected_subheadings.split('~')
    assert expected_subheadings_list == actual_subheadings_list, f"{expected_subheadings_list} and {actual_subheadings_list} do not match"


@step('I verify if the slider is present and the four slides are present')
def verify_slider_present(context):
    slider_element = WebDriverWait(context.driver,10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='carousel__viewport'][.//ul[@class='carousel__list' and @id='s0-1-0-48-1-2-4-17[0[0]]-0[1]-2-@match-media-0-@ebay-carousel-list']]")),"Slider Not Present")

    slides = WebDriverWait(context.driver,10).until(EC.presence_of_all_elements_located((By.XPATH,"//ul[@class='carousel__list' and @id='s0-1-0-48-1-2-4-17[0[0]]-0[1]-2-@match-media-0-@ebay-carousel-list']//li[@class='carousel__snap-point vl-carousel__item']")))


@step('I click on the previous button and verify the functionality')
def click_previous_button(context):
    previous_button = context.driver.find_element(By.XPATH,"//button[@class='carousel__control carousel__control--prev' and @aria-label='Go to previous banner']")
    WebDriverWait(context.driver,10).until(EC.presence_of_element_located((By.XPATH, "//ul[@class='carousel__list' and @id='s0-1-0-48-1-2-4-17[0[0]]-0[1]-2-@match-media-0-@ebay-carousel-list']//li[1]")))
    previous_button.click()
    active_slide = context.driver.find_element(By.XPATH,"//ul[@class='carousel__list' and @id='s0-1-0-48-1-2-4-17[0[0]]-0[1]-2-@match-media-0-@ebay-carousel-list']//li[@class='carousel__snap-point vl-carousel__item' and not(@aria-hidden)]")
    last_slide = context.driver.find_element(By.XPATH,"//ul[@class='carousel__list' and @id='s0-1-0-48-1-2-4-17[0[0]]-0[1]-2-@match-media-0-@ebay-carousel-list']//li[4]")

    assert active_slide == last_slide, "Previous button not working as expected"


@step('I click on the Pause button and verify the functionality')
def click_pause_button(context):
    pause_button = context.driver.find_element(By.XPATH,"//button[@aria-label='Pause Banner Carousel']")
    first_slide = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                            "//ul[@class='carousel__list' and @id='s0-1-0-48-1-2-4-17[0[0]]-0[1]-2-@match-media-0-@ebay-carousel-list']//li[1]")))
    pause_button.click()
    active_slide = context.driver.find_element(By.XPATH,"//ul[@class='carousel__list' and @id='s0-1-0-48-1-2-4-17[0[0]]-0[1]-2-@match-media-0-@ebay-carousel-list']//li[@class='carousel__snap-point vl-carousel__item' and not(@aria-hidden)]")

    assert first_slide == active_slide, "Pause button not working as expected"


@step('I intentionally fail this step')
def intentional_fail(context):
    assert False, "Intentionally failing this step"


@step('I verify if the items in the first {max_page} pages are related to {item_name}')
def page_validation(context, max_page, item_name):
    max_page_number = int(max_page)
    current_page = context.driver.find_element(By.XPATH, f"//ol[@class='pagination__items']/li/a[text()='1']")
    current_page_number = int(current_page.text)
    issues = []

    while current_page_number < max_page_number:
        list_of_all_items = context.driver.find_elements(By.XPATH, f"//div[@class='s-item__title']//span[@role='heading']")
        for item in list_of_all_items:
            item_title = item.text
            if item_name.lower() not in item_title.lower():
                issues.append(f"{item_title} does not contain {item_name} and hence not related")

        next_page = context.driver.find_element(By.XPATH,"//a[@aria-label='Go to next search page']")
        next_page.click()
        time.sleep(2)

        current_page = context.driver.find_element(By.XPATH,"//a[@class='pagination__item' and @aria-current]")
        current_page_number = int(current_page.text)

    if issues:
        for issue in issues:
            print(issue)
