from behave import *


@then(u'Total number of people where height is greater than {height:d} matches {number_of_people:d}')
def step_impl(context, height, number_of_people):
    response_json = context.response.json()

    # count total number of people where height is greater than given height
    total_number = 0
    for person in response_json['results']:
        if int(person['height']) > height:
            total_number += 1

    assert total_number == number_of_people, f"Total number '{total_number}' of people where height greater than '{height}'" \
                                             f" doesn't match '{number_of_people}'"


@then(u'List of people whose height is greater than {height:d} is {people_list}')
def step_impl(context, height, people_list):
    response_json = context.response.json()

    # get list of people with height higher than given
    people = []
    for person in response_json['results']:
        if int(person['height']) > height:
            people.append(person['name'])

    people.sort()

    # convert given string to an actual python list
    expected_people_list = people_list.replace(', ', ',').split(',')
    expected_people_list.sort()

    assert people == expected_people_list, f"Expected people whose height higher than {height} don't mutch:" \
                                  f" expected list: '{expected_people_list}', actual list: '{people}'"
