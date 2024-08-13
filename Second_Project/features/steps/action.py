from behave import step
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


@step('I navigate to the website')
def navigate_to_website(context):
    context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    context.driver.get('https://www.elated.com/res/File/articles/development/javascript/jquery/drag-and-drop-with-jquery-your-essential-guide/card-game.html')


@step('I drag and drop all the elements to right places')
def drag_and_drop(context):
    list_draggable = context.driver.find_elements(By.XPATH, "//div[@id='cardPile']/div")
    droppable_places = context.driver.find_elements(By.XPATH, "//div[@id='cardSlots']/div")
    for element in list_draggable:
        element_index = int(element.text)
        target_element = droppable_places[element_index-1]
        action_items = ActionChains(context.driver)
        action_items.click_and_hold(element).move_to_element(target_element).release().perform()

