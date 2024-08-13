Feature: Testing the behaviour of Ebay Slider

  Scenario: Test if all the four slides in the slider are present and visible
    Given I navigate to Ebay website
    Then I verify if the slider and slides are present

  Scenario: Test if the Previous button is working
    Given I navigate to Ebay website
    Then I verify if the slider and slides are present
    Then I verify that the Previous button is working

  Scenario: Test if the Next button is working
    Given I navigate to Ebay website
    Then I verify if the slider and slides are present
    Then I verify that the Next button is working

  Scenario: Test if the Pause button is working
    Given I navigate to Ebay website
    Then I verify if the slider and slides are present
    Then I verify that the Pause button is working