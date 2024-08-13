import time
from telnetlib import EC

from behave import step
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@step('I navigate to Ebay website')
def navigate(context):
    context.driver.get(context.url)
    time.sleep(2)


@step('I search for a dress')
def search_dress(context):
    search_box = context.driver.find_element(By.XPATH,"//input[@aria-label='Search for anything']")
    search_box.send_keys("dress")
    search_icon = context.driver.find_element(By.XPATH, "//input[@id='gh-btn']")
    search_icon.click()
    time.sleep(5)


@step('on the first {n} pages validate if the results are {item_name} related')
def validate_search(context, n, item_name):
    current_page = context.driver.find_element(By.XPATH, "//a[@class='pagination__item' and @aria-current]")
    current_page_num = int(current_page.text)
    print(current_page_num)

    total_page_text = int(n)

    issues = []
    while current_page_num < (total_page_text+1):
        print(f"Validating items on page {current_page_num}")
        items_list = context.driver.find_elements(By.XPATH,"//div[@class='s-item__title']/span")
        for item in items_list:
            item_title = item.text
            if item_title:
                if item_name.lower() not in item_title.lower():
                    issues.append(f"The word {item_name} is not in {item_title}")
        time.sleep(3)
        next_page = context.driver.find_element(By.XPATH,"//a[@aria-label='Go to next search page']")
        next_page.click()

        time.sleep(2)

        current_page = context.driver.find_element(By.XPATH, "//a[@class='pagination__item' and @aria-current]")
        current_page_num = int(current_page.text)
        print(f"Moving to page {current_page_num}")

    for issue in issues:
        print(issue)


@step('i land on {landing_page} page validate if the items are related to {item_text} until {max_page} pages')
def from_landing_page_search_validation(context, landing_page, item_text, max_page):
    landing_page_text = int(landing_page)
    max_page_text = int(max_page)

    landing_page_element = context.driver.find_element(By.XPATH, f"//a[text()={landing_page}]")
    landing_page_element.click()
    time.sleep(5)

    issues = []

    while landing_page_text < max_page_text:
        print(f"Entered page {landing_page_text}")
        items_list = context.driver.find_elements(By.XPATH,"//div[@class='s-item__title']/span")
        for item in items_list:
            item_title = item.text
            if item_title:
                if item_text.lower() not in item_title.lower():
                    issues.append(f"The word {item_text} is not in {item_title}")

        next_button = context.driver.find_element(By.XPATH, "//a[@aria-label='Go to next search page']")
        next_button.click()
        print("Clicked on the Next Button")
        time.sleep(5)

        landing_page_element = context.driver.find_element(By.XPATH,"//a[@aria-current and @class='pagination__item']")
        temp = landing_page_element.text
        landing_page_text = int(temp)

    print(issues)
        

@step('I apply filter {sub} under the category {category_name}')
def apply_filter(context, sub, category_name):
    check_box = context.driver.find_element(By.XPATH, f"//li[@class='x-refine__main__list '][.//div[text()='{category_name}']]//div[@class='x-refine__select__svg'][.//span[text()='{sub}']]//input")
    check_box.click()


@step('I click on the {navigation_link}')
def click_nav(context, navigation_link):
    ...


@step('I verify the {title} of the landing page')
def verify_title(context, title):
    ...
        

@step('I apply filter category {category_name} with sub category {sub}')
def apply_filters_checkbox(context, category_name, sub):
    filter_checkbox = context.driver.find_element(By.XPATH, f"//li[@class='x-refine__main__list '][.//div[text()='{category_name}']]//input[@aria-label='{sub}']")
    if category_name == 'Sleeve Length' or category_name == 'Occasion' or category_name == 'Style' or category_name == 'Pattern':
        label = context.driver.find_element(By.XPATH, f"//h3[@class='x-refine__item__title'][.//div[text()='{category_name}']]")
        label.click()
        time.sleep(2)
        filter_checkbox.click()
        time.sleep(5)
    else:
        filter_checkbox.click()
        time.sleep(5)


@step('I verify if the dresses displayed are with {category} as {sub}')
def verify_filters(context, category, sub):
    main_window = context.driver.current_window_handle

    list_of_all_items = context.driver.find_elements(By.XPATH, "//li[contains(@id,'item')]")

    issues = []

    for item in list_of_all_items:
        item_title = item.find_element(By.XPATH, ".//span[@role='heading']").text
        item_url = item.find_element(By.XPATH, ".//a[@class='s-item__link']").get_attribute('href')

        context.driver.execute_script(f"window.open('{item_url}');")
        context.driver.switch_to.window(context.driver.window_handles[-1])

        try:
            all_labels = WebDriverWait(context.driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, "//dt[@class='ux-labels-values__labels'][.//div[@class='ux-labels-values__labels-content']]"))
            )
            all_values = WebDriverWait(context.driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, "//dd[@class='ux-labels-values__values'][.//div[@class='ux-labels-values__values-content']]"))
            )

            all_label_texts = []
            for label in all_labels:
                all_label_texts.append(label.text)

            all_value_texts = []
            for value in all_values:
                all_value_texts.append(value.text)

            item_specifications = dict(zip(all_label_texts, all_value_texts))

            if category in item_specifications:
                actual_value = item_specifications[category].lower()
                expected_value = sub.lower()
                if expected_value != actual_value:
                    issues.append(f"The {item_title} is not under the subcategory {sub} but has the {category} as {actual_value}")
            else:
                issues.append(f"The {item_title} does not have a {category} specified")

        except Exception as e:
            issues.append(f"Error processing {item_title}: {str(e)}")

        context.driver.close()
        context.driver.switch_to.window(main_window)

    if issues:
        for issue in issues:
            print(issue + "\n")

