from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_all_elements_located
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import step


@step('I verify if the slider and slides are present')
def slides_present(context):
    slider = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//ul[@class='carousel__list' and @id='s0-1-0-48-1-2-4-17[0[0]]-0[1]-2-@match-media-0-@ebay-carousel-list']")),
        "Slider element is not found")


@step('I verify that the Previous button is working')
def verify_previous_button(context):
    slides_list = context.driver.find_elements(By.XPATH,"//ul[@class='carousel__list' and @id='s0-1-0-48-1-2-4-17[0[0]]-0[1]-2-@match-media-0-@ebay-carousel-list']/li")
    WebDriverWait(context.driver,10).until(EC.presence_of_element_located((By.XPATH, "//ul[@class='carousel__list' and @id='s0-1-0-48-1-2-4-17[0[0]]-0[1]-2-@match-media-0-@ebay-carousel-list']/li[1]")))

    previous_button = context.driver.find_element(By.XPATH,"//button[@aria-label='Go to previous banner']")
    previous_button.click()

    current_active_slide = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.XPATH,"//ul[@class='carousel__list' and @id='s0-1-0-48-1-2-4-17[0[0]]-0[1]-2-@match-media-0-@ebay-carousel-list']/li[@class='carousel__snap-point vl-carousel__item' and not(@aria-hidden)]")))
    expected_previous_slide = slides_list[-1]

    assert current_active_slide == expected_previous_slide, "The previous button did not navigate to the expected slide."

    print("Previous button is working correctly and navigated to the last slide.")


@step('I verify that the Next button is working')
def verify_next_button(context):
    slides_list = context.driver.find_elements(By.XPATH,
                                               "//ul[@class='carousel__list' and @id='s0-1-0-48-1-2-4-17[0[0]]-0[1]-2-@match-media-0-@ebay-carousel-list']/li")
    WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                            "//ul[@class='carousel__list' and @id='s0-1-0-48-1-2-4-17[0[0]]-0[1]-2-@match-media-0-@ebay-carousel-list']/li[1]")))

    next_button = context.driver.find_element(By.XPATH, "//button[@aria-label='Go to next banner']")
    next_button.click()

    current_active_slide = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                                                   "//ul[@class='carousel__list' and @id='s0-1-0-48-1-2-4-17[0[0]]-0[1]-2-@match-media-0-@ebay-carousel-list']/li[@class='carousel__snap-point vl-carousel__item' and not(@aria-hidden)]")))
    expected_next_slide = slides_list[1]

    assert current_active_slide == expected_next_slide, "The next button did not navigate to the expected slide."

    print("Next button is working correctly and navigated to the second slide.")


@step('I verify that the Pause button is working')
def verify_pause_button(context):
    slides_list = context.driver.find_elements(By.XPATH,
                                               "//ul[@class='carousel__list' and @id='s0-1-0-48-1-2-4-17[0[0]]-0[1]-2-@match-media-0-@ebay-carousel-list']/li")
    WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                            "//ul[@class='carousel__list' and @id='s0-1-0-48-1-2-4-17[0[0]]-0[1]-2-@match-media-0-@ebay-carousel-list']/li[1]")))

    pause_button = context.driver.find_element(By.XPATH, "//button[@aria-label='Pause Banner Carousel']")
    pause_button.click()

    # Locate the currently active slide
    current_active_slide = context.driver.find_element(By.XPATH,
                                                       "//ul[@class='carousel__list' and @id='s0-1-0-48-1-2-4-17[0[0]]-0[1]-2-@match-media-0-@ebay-carousel-list']/li[@class='carousel__snap-point vl-carousel__item' and not(@aria-hidden)]")

    # Locate the first slide
    first_slide = context.driver.find_element(By.XPATH,
                                              "//ul[@class='carousel__list' and @id='s0-1-0-48-1-2-4-17[0[0]]-0[1]-2-@match-media-0-@ebay-carousel-list']/li[1]")

    # Compare the current active slide with the first slide
    assert current_active_slide == first_slide, "The pause button did not stop the carousel from moving."

    # Optional: Print a success message for debugging
    print("Pause button is working correctly and the carousel did not move.")

