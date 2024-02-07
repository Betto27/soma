from behave import *
from nose.tools import assert_equal
from tabuada import calc


res = 0

@given('que acesso a calculadora')
def step_impl(context):
    pass

@when('quando insiro {num1} + {num2}')
def step_impl(context, num1, num2):
    res = calc(num1, num2)


@then('o resultado é {numR}')
def step_impl(context, numR, res):
    assert_equal(numR)

