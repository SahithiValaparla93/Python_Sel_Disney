Feature: Ebay Regression testcases

  Scenario: Click on all the navigation links
    Given I am navigating to ebay website
    And I search for a dress
    Then I verify if the items displayed are related to dress


   Scenario Outline: Verify filter validation
     Given I am navigating to ebay website
     And I search for a dress
     And I apply filter <subcategory> under the <category>
     Then I validate if the items displayed are <subcategory> under <category>
     Examples:
     |subcategory|category|
     |Short|Dress Length|
     |Zara|Brand|


   Scenario: Click all the navigation links using context table
     Given I am navigating to ebay website
     Then I click on the following navigation links and verify the titles
     |navlink|pagetitle|
     |Help & Contact|Security Measure|

   Scenario: Validate the items on first three pages
     Given I am navigating to ebay website
     And I search for a dress
     And I validate if the items displayed are related to dress in the first 7 pages


   Scenario: Validate the items on given number of pages when landed on 2nd page
     Given I am navigating to ebay website
     And I search for a dress
     And I validate if the items displayed are related to dress until 8 pages given i am on 4 page


   Scenario: Verify if the slider is visible
     Given I am navigating to ebay website
     And I verify if the slider is visible

   Scenario: Verify if the previous button is working
     Given I am navigating to ebay website
     And I verify if the slider is visible
     And I click on Previous button and verify if its functional

