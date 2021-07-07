Feature: Verify Registration Page

  @Sanity
  Scenario: Enter InCorrect Registration Details
    Given Launch application page
    When User enters "username"
    And User enters "password"
    And User enters "email"
    And User enters "confirm password"

  @Regression
  Scenario: Enter Correct Registration Details
    Given Launch application page
    When User enters "username"
    And User enters "password"
    And User enters "email"
    And User enters "confirm password"