from behave import *
import requests


@given(u'Get to "/people" url')
def step_impl(context):
    context.url = "https://swapi.dev/api/people/"
    context.response = requests.get(context.url)


@then(u'Response status code is {status_code:d}')
def step_impl(context, status_code):
    assert context.response.status_code == status_code, f"Wrong response status code received:" \
                                                        f"expected status code is '{status_code}', " \
                                                        f"received status code is '{context.response.status_code}'"
