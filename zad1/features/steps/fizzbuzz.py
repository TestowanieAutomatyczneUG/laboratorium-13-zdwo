from behave import *
from zad1a.FizzBuzz import FizzBuzz


@given("FizzBuzz game")
def step_impl(context):
    context.fizzbuzz = FizzBuzz()


@when("3")
def step_impl(context):
    context.res = 3


@when("5")
def step_impl(context):
    context.res = 5


@when("15")
def step_impl(context):
    context.res = 15


@when("7")
def step_impl(context):
    context.res = 7


@when("20")
def step_impl(context):
    context.res = 20


@then("Fizz")
def step_impl(context):
    assert context.fizzbuzz.game(context.res) == "Fizz"


@then("Buzz")
def step_impl(context):
    assert context.fizzbuzz.game(context.res) == "Buzz"


@then("FizzBuzz")
def step_impl(context):
    assert context.fizzbuzz.game(context.res) == "FizzBuzz"


@then("7")
def step_impl(context):
    assert context.fizzbuzz.game(context.res) == 7



