Feature: showing off behave


  Scenario: Skiplagged page title test
    Given a user is in skiplagged.com
    Then skiplagged.com page title should be 'Skiplagged: The smart way to find cheap flights.'

  Scenario: Skiplagged currency options test
    Given a user is in skiplagged.com
    Then default currency would be 'USD'
    When a user selects currency options
    Then a user should be seeing the following currency list
      | Currency |
      | AUD      |
      | BRL      |
      | CAD      |
      | EUR      |
      | GBP      |
      | HKD      |
      | INR      |
      | MYR      |
      | SEK      |
      | SGD      |
      | USD      |
    And a user should be able to select 'EUR' as currency


  Scenario: Skiplagged one way trip search test-1
    Given a user is in skiplagged.com
    When a user selects one way trip
    And a user selects 'NYC' as source airport
    And a user selects 'CMB' as destination airport
    And a user selects 'September 2020 30' as date of departure
    And  a user clicks on search flights button
    Then a user should be navigated to flight search results page

  Scenario Outline: Skiplagged one way trip search tests
    Given a user is in skiplagged.com
    When a user selects <sourceAirport>, <destinationAirport>, and <departureDate>
    And  a user clicks on search flights button
    Then a user should be navigated to flight search results page
    Examples:
      | sourceAirport | destinationAirport | departureDate     |
      | NYC           | CMB                | September 2020 30 |
      | LGA           | FRA                | November 2020 1   |

  Scenario: Skiplagged round way trip search test-1
    Given a user is in skiplagged.com
    When a user selects round trip
    And a user selects 'NYC' as source airport
    And a user selects 'CMB' as destination airport
    And a user selects 'September 2020 30' as date of departure
    And a user selects 'December 2020 31' as date of arrival
    And  a user clicks on search flights button
    Then a user should be navigated to flight search results page

  Scenario Outline: Skiplagged round way trip search tests
    Given a user is in skiplagged.com
    When a user selects <sourceAirport>, <destinationAirport>, <departureDate> and <arrivalDate>
    And  a user clicks on search flights button
    Then a user should be navigated to flight search results page
    Examples:
      | sourceAirport | destinationAirport | departureDate     | arrivalDate      |
      | NYC           | CMB                | September 2020 30 | November 2020 10 |
      | LGA           | FRA                | November 2020 1   | December 2020 25 |




