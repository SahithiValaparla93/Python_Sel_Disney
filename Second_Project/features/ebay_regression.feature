Feature: Ebay Regression test cases

  Scenario: Check if one of the navigation links redirects us to the correct page
    Given I am navigating to ebay website
    And when I click on the below links
      | Link Text    | Expected Title                                      |
      | Daily Deals  | Daily Deals on eBay \| Best deals and Free Shipping |
      |  Brand Outlet| Brand Outlet products for sale \| eBay |


  Scenario: Filtering and Validating
    Given I am navigating to ebay website
    And I search for a dress
    Then I verify if the items displayed are dress related

  Scenario: Apply filter and validate if the items displayed are actually filtered
    Given I am navigating to ebay website
    And I search for a dress
    And I apply the filter Short under the Dress Length
    Then I verify if the items are with Short under the Dress Length

  Scenario Outline: Click on the Shop by category link and verify the subheadings under the headings
    Given I am navigating to ebay website
    And I click on Shop By Category Dropdown
    Then I verify if the <Heading> has the <expected_subheadings>

    Examples:
    | Heading                | expected_subheadings                                         |
    | Motors                 | Parts & accessories~Cars & trucks~Motorcycles~Other vehicles |
    | Clothing & Accessories | Women~Men~Handbags~Collectible Sneakers                      |
    | Sporting goods         | Hunting Equipment~Golf Equipment~Outdoor sports~Cycling Equipment |
    | Electronics            | Computers, Tablets & Network Hardware~Cell Phones, Smart Watches & Accessories~Video Games & Consoles~Cameras & Photo |
    | Business & Industrial  | Modular & Pre-Fabricated Buildings~Test, Measurement & Inspection Equipment~Heavy Equipment, Parts & Attachments~Restaurant & Food Service |
    | Jewelry & Watches      | Luxury Watches~Wristwatches~Fashion Jewelry~Fine Jewelry    |
    | Collectibles & Art     | Trading Cards~Collectibles~Coins & Paper Money~Sports Memorabilia |
    | Home & garden          | Yard, Garden & Outdoor Living Items~Tools & Workshop Equipment~Home Improvement~Kitchen, Dining & Bar Supplies |
    | Other categories       | Books, Movies & Music~Toys & Hobbies~Health & Beauty~Baby Essentials |

  Scenario: Verify the Slider elements presence and visibility
    Given I am navigating to ebay website
    Then I verify if the slider is present and the four slides are present

  Scenario: Verify if the previous button is working as expected
    Given I am navigating to ebay website
    Then I verify if the slider is present and the four slides are present
    And I click on the previous button and verify the functionality


  Scenario: Verify if the Pause button is working as expected
    Given I am navigating to ebay website
    Then I verify if the slider is present and the four slides are present
    And I click on the Pause button and verify the functionality

  Scenario: I intentionally fail this step
    And I intentionally fail this step

  Scenario: Collect all the dresses in first three pages
    Given I am navigating to ebay website
    And I search for a dress
    And I apply the filter Short under the Dress Length
    Then I verify if the items in the first 4 pages are related to dress
