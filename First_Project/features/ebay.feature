Feature: Ebay Regression Testcases

 Scenario Outline: Click on the navigation links
    Given Navigate to Ebay
    And Click on the link <link_name>
    Then verify that the title of the page is <page_title>

   Examples:
   |link_name|page_title|
   |Daily Deals|Daily Deals on eBay \| Best deals and Free Shipping|
   |Gift Cards|eBay Gift Cards \| eBay.com|
   |Brand Outlet|Brand Outlet products for sale \| eBay|
   |Help & Contact|Security Measure|
   |Sell|Selling on eBay \| Electronics, Fashion, Home & Garden \| eBay|


 Scenario: Filtering the items
   Given Navigate to Ebay
   And Enter dress in the search bar
   Then select the filter Sleeve Length by Half Sleeve

 Scenario: Filtering the items through radiobuttons
   Given Navigate to Ebay
   And Enter dress in the search bar
   Then select the Buying Format by Auction
   Then select the Item Location by North America

 Scenario: Color Filtering
   Given Navigate to Ebay
   And Enter dress in the search bar
   Then I click Black color from the color picker

 Scenario: Search validation
   Given Navigate to Ebay
   And Enter dress in the search bar
   Then verify if each item retrieved is related to dress

 Scenario: While loop search validation
   Given Navigate to Ebay
   And Enter dress in the search bar
   Then First 3 pages with while loop are dress related

 Scenario: Search functionality on few pages when landed not on the first one
   Given Navigate to Ebay
   And Enter dress in the search bar
   Then land on 3 page and verify if the items titles in each page has the word dress until page 6

  Scenario Outline: Verify subheadings under each category
    Given Navigate to Ebay
    When I click on the Shop by category dropdown
    Then I should see the subheadings <expected_subheadings> under <category>

    Examples:
    | category               | expected_subheadings                                         |
    | Motors                 | Parts & accessories,Cars & trucks,Motorcycles,Other vehicles |
    | Clothing & Accessories | Women,Men,Handbags,Collectible Sneakers                      |
    | Sporting goods         | Hunting Equipment,Golf Equipment,Outdoor sports,Cycling Equipment |
    | Electronics            | Computers,Tablets & Network Hardware,Cell Phones,Smart Watches & Accessories,Video Games & Consoles,Cameras & Photo |
    | Business & Industrial  | Modular & Pre-Fabricated Buildings,Test,Measurement & Inspection Equipment,Heavy Equipment,Parts & Attachments,Restaurant & Food Service |
    | Jewelry & Watches      | Luxury Watches,Wristwatches,Fashion Jewelry,Fine Jewelry    |
    | Collectibles & Art     | Trading Cards,Collectibles,Coins & Paper Money,Sports Memorabilia |
    | Home & garden          | Yard,Garden & Outdoor Living Items,Tools & Workshop Equipment,Home Improvement,Kitchen,Dining & Bar Supplies |
    | Other categories       | Books,Movies & Music,Toys & Hobbies,Health & Beauty,Baby Essentials |


  Scenario Outline: Validate Filtering functionality
   Given Navigate to Ebay
   And Enter dress in the search bar
   Then I filter by <Category> which has the sub category <Sub>
   Then I verify if the dresses with <Category> are related to <Sub>

    Examples:
    |Category|Sub|
    |Brand|Zara|



