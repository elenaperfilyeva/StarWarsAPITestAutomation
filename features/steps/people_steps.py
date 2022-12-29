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
