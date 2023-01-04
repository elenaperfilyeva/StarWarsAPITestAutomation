from behave import *
import requests

from utilities.configurations import *


@given(u'Get to "{url}" url')
def step_impl(context, url):
    context.url = get_config()['API']['endpoint'] + url
    context.response = requests.get(context.url)


@then(u'Response status code is {status_code:d}')
def step_impl(context, status_code):
    assert context.response.status_code == status_code, f"Wrong response status code received:" \
                                                        f"expected status code is '{status_code}', " \
                                                        f"received status code is '{context.response.status_code}'"
