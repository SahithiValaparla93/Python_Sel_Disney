Feature: Ebay Regression testing

  Scenario: Apply Filter and Validate the title
    Given I navigate to ebay website
    And I search for shoes
    And I apply the filter Nike under Brand
    And I apply the filter Beige under Color
    Then I verify if the title of the item matches the actual title