# Created by dell at 28.12.2022
Feature: Verify that the total number of people where height is greater than 200 matches the expected count

  Scenario: Total number of people where height is greater than 200 matches 1 verification
    Given Get to "/people" url
    Then Total number of people where height is greater than 200 matches 1
