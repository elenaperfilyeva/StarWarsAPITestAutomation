# Created by dell at 28.12.2022
Feature: Verify people whose height is greater than 200

  Scenario: People whose height is greater than 200 are
    Given Get to "/people" url
    Then List of people whose height is greater than 200 is Darth Vader
