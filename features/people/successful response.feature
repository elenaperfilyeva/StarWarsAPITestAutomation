# Created by dell at 28.12.2022
Feature: Verify that the “people” endpoint is returning a successful response

  Scenario: “people” endpoint returns a successful response verification
    Given Get to "/people" url
    Then Response status code is 200