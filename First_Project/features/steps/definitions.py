from behave import step
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@step('Navigate to Ebay')
def navigate_to_ebay(context):
    context.driver.get(context.url)


@step('Click on the link {my_var}')
def click_on_link_deals(context, my_var):
    daily_deals = context.driver.find_element(By.XPATH, f"//a[normalize-space(text())='{my_var}']")
    daily_deals.click()


@step('verify that the title of the page is {expected_title}')
def verify_title_daily_deals(context, expected_title):
    actual_title = context.driver.title
    assert actual_title == expected_title, "Title does not match"


@step('Enter {dress} in the search bar')
def enter_text_in_search_bar(context, dress):
    search_bar = context.driver.find_element(By.XPATH, "//input[@aria-label='Search for anything']")
    search_bar.send_keys(dress)
    search_button = context.driver.find_element(By.XPATH, "//input[@id='gh-btn']")
    search_button.click()


@step('select the filter {Occasion} by {Travel}')
def select_filter(context, Occasion, Travel):
    sleep(2)
    check_box = context.driver.find_element(By.XPATH,
                                            f"//li[@class='x-refine__main__list '][.//div[text()='{Occasion}']]//div[.//span[text()='{Travel}']]//input")
    check_box.click()


@step('select the {filters} by {radio}')
def select_filter(context, filters, radio):
    radio_button = context.driver.find_element(By.XPATH,
                                               f"//li[@class='x-refine__main__list '][.//div[text()='{filters}']]//div[@class='x-refine__select__svg'][.//span[text()='{radio}']]//input")
    radio_button.click()
    sleep(5)


@step('I filter by {category} which has the sub category {desired_size}')
def size_filter(context, category, desired_size):
    size_filter_option = context.driver.find_element(By.XPATH, f"//li[@class='x-refine__main__list '][.//div[@class='x-refine__item__title-container' and text()='{category}']]//div[@class='x-refine__select__svg'][.//span[text()='{desired_size}']]//input")
    size_filter_option.click()
    sleep(3)


@step('I click {Color} color from the color picker')
def pick_color(context, Color):
    desired_color = context.driver.find_element(By.XPATH,
                                                f"//li[@class='x-refine__main__list '][.//div[text()='Color']]//ul[@class='x-color-picker__body']//a[contains(@href,'{Color}')]")
    desired_color.click()
    sleep(5)


@step('verify if each item retrieved is related to {dress}')
def search_validate(context, dress):
    pages = context.driver.find_elements(By.XPATH, "//ol[@class='pagination__items']/li")
    print(len(pages))
    issues = []
    for page in pages:
        items = context.driver.find_elements(By.XPATH,
                                             "//li[@class='s-item s-item__pl-on-bottom']//div[@class='s-item__title']//span")
        for item in items:
            item_title = item.text
            if dress.lower() not in item_title.lower():
                issues.append(f'{item_title} does not contain the word {dress}')
    if issues:
        print('Below are the issues found:')
        for issue in issues:
            print(issue)
        raise Exception(f'Above is the list of items which do not have the word dress')


@step('First {total_pages} pages with while loop are {desired_item} related')
def search_test(context, total_pages, desired_item):
    current_page = context.driver.find_element(By.XPATH, "//a[@class='pagination__item' and @aria-current]")
    current_page_text = current_page.text

    total_pages_text = int(total_pages)

    issues = []

    while int(current_page_text) < int(total_pages_text):
        print(f'Right now in {current_page_text} page')

        items = context.driver.find_elements(By.XPATH,
                                             "//li[@class='s-item s-item__pl-on-bottom']//div[@class='s-item__title']//span")
        for item in items:
            item_title = item.text
            if item_title:
                if desired_item.lower() not in item_title.lower():
                    issues.append(f'{item_title} does not have the word {desired_item}')

        next_page = context.driver.find_element(By.XPATH, "//a[@aria-label='Go to next search page']")
        next_page.click()
        sleep(2)

        current_page = context.driver.find_element(By.XPATH, "//a[@class='pagination__item' and @aria-current]")
        current_page_text = current_page.text

    if issues:
        print(issues)
        raise Exception(f'{issues}')



@step('land on {landing_page} page and verify if the items titles in each page has the word {desired_text} until page {desired_page}')
def verify_search_from_landing_page(context, landing_page, desired_text, desired_page):
    landing_page_element = context.driver.find_element(By.XPATH, f"//a[text()='{landing_page}']")
    landing_page_element_text = landing_page_element.text
    landing_page_element.click()

    issues = []
    while int(landing_page_element_text) < int(desired_page):
        print(f'Right now in {landing_page_element_text} page')
        items = context.driver.find_elements(By.XPATH,
                                             "//li[@class='s-item s-item__pl-on-bottom']//div[@class='s-item__title']//span")
        for item in items:
            item_title = item.text
            if item_title:
                if desired_text.lower() not in item_title.lower():
                    issues.append(f'{item_title} does not have the word {desired_text}')

        next_page = context.driver.find_element(By.XPATH, "//a[@aria-label='Go to next search page']")
        next_page.click()
        print('Clicked on the next page')
        sleep(2)

        landing_page_element = context.driver.find_element(By.XPATH, "//a[@class='pagination__item' and @aria-current]")
        landing_page_element_text = landing_page_element.text

    if issues:
        print(issues)
        raise Exception(f'{issues}')


@step('I click on the Shop by category dropdown')
def hover_shop_by_category(context):
    shop_by_category = context.driver.find_element(By.XPATH, "//button[@id='gh-shop-a']")
    shop_by_category.click()
    sleep(4)


@step('I should see the subheadings {expected_subheadings} under {category}')
def verify_sub_category(context, expected_subheadings, category):
    actual_subheadings = context.driver.find_elements(By.XPATH,
                                                      f"//h3[@class='gh-sbc-parent'][a[text()='{category}']]/following-sibling::ul[1]/li/a")
    expected_subheadings_list = expected_subheadings.split(',')
    actual_subheadings_list = []
    for sub in actual_subheadings:
        actual_subheadings_list.append(sub.get_attribute("textContent").strip())

    assert actual_subheadings_list == expected_subheadings_list, f"Expected subheadings: {expected_subheadings_list}, Actual subheadings: {actual_subheadings_list}"


@step('I verify if the dresses with {key_name} are related to {expected_value}')
def verify_the_filter_functionality(context, key_name, expected_value):
    list_items = context.driver.find_elements(By.XPATH, "//li[contains(@id,'item')]")

    main_window = context.driver.current_window_handle
    wait = WebDriverWait(context.driver, 10)

    issues = []

    for item in list_items:
        item_title = item.find_element(By.XPATH, ".//span[@role='heading']").text
        product_url = item.find_element(By.XPATH, ".//a[@class='s-item__link']").get_attribute("href")

        context.driver.execute_script(f"window.open('{product_url}')")
        context.driver.switch_to.window(context.driver.window_handles[-1])

        all_labels = context.driver.find_elements(By.XPATH, "//dt[@class='ux-labels-values__labels'][.//span]")
        all_values = context.driver.find_elements(By.XPATH, "//dd[@class='ux-labels-values__values'][.//span]")

        all_labels_text = []
        all_values_text = []

        for i in all_labels:
            all_labels_text.append(i.text)

        for i in all_values:
            all_values_text.append(i.text)

        item_specs = dict(zip(all_labels_text, all_values_text))

        if key_name not in item_specs.keys():
            issues.append(f"{item_title} does not have any specification related to {key_name}")
        elif (item_specs[key_name]).lower() != expected_value.lower():
            issues.append(f"{item_title} does not have the {key_name} as {expected_value}")

        context.driver.close()

        context.driver.switch_to.window(main_window)

    if issues:
        raise Exception(f'{issues}')
