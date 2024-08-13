Feature: Practicing Regression test cases

  Scenario: Click on the Daily Deals Link and verify you landed on the right page
    Given I navigate to Ebay website
    And I click on the navigation_link
    Then I verify the title of the landing page

  Scenario: Click on all the navigation links using generalized xpath

  Scenario: Click on all the navigation links using scenario outline

  Scenario Outline: Search for dress and then apply filter with generalized xpath
    Given I navigate to Ebay website
    And I search for a dress
    Then I apply filter <Sub_Category> under the category <Main_Category>

    Examples:
    |Sub_Category|Main_Category|
    |Short|Dress Length|
    |Sleeveless|Sleeve Length|
    |New with tags|Condition|


  Scenario: Search for dress and see if the items in first three pages are valid
    Given I navigate to Ebay website
    And I search for a dress
    Then on the first 3 pages validate if the results are dress related


  Scenario: Search for dress and see if the items in given pages are valid
    Given I navigate to Ebay website
    And I search for a dress
    Then i land on 5 page validate if the items are related to dress until 9 pages


  Scenario: Verify filter validation
    Given I navigate to Ebay website
    And I search for a dress
    And I apply filter category Dress Length with sub category Short
    Then I verify if the dresses displayed are with Dress Length as Short