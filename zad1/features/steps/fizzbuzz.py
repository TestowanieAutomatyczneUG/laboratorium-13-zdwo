from behave import *
from zad1.FizzBuzz import FizzBuzz


@given("FizzBuzz game")
def step_impl(context):
    context.fizzbuzz = FizzBuzz()


@when("3")
def step_impl(context):
    context.num = 3


@when("5")
def step_impl(context):
    context.num = 5


@when("15")
def step_impl(context):
    context.num = 15


@when("7")
def step_impl(context):
    context.num = 7


@when("20")
def step_impl(context):
    context.num = 20


@then("Fizz")
def step_impl(context):
    assert context.fizzbuzz.game(context.num) == "Fizz"


@then("Buzz")
def step_impl(context):
    assert context.fizzbuzz.game(context.num) == "Buzz"


@then("FizzBuzz")
def step_impl(context):
    assert context.fizzbuzz.game(context.num) == "FizzBuzz"


@then("7")
def step_impl(context):
    assert context.fizzbuzz.game(context.num) == 7



