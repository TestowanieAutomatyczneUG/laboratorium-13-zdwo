from behave import *
from assertpy import assert_that


@when("abc")
def step_impl(context):
    context.word = "abc"


@when("pack my box with dozen liquor jugs")
def step_impl(context):
    context.word = "pack my box with dozen liquor jugs"


@when("pack my box with five dozen liquor jugs")
def step_impl(context):
    context.word = "pack my box with five dozen liquor jugs"


@when("the quick brown fox jumps over the lazy dog")
def step_impl(context):
    context.word = "the quick brown fox jumps over the lazy dog"


@when("word is none")
def step_impl(context):
    context.word = None


@when("arg is the wrong type")
def step_impl(context):
    context.word = ()


@when("word is empty")
def step_impl(context):
    context.word = ""


@when("word is int")
def step_impl(context):
    context.word = 1


@then("not a pangram")
def step_impl(context):
    assert context.pangram.check(context.word) == False


@then("is pangram")
def step_impl(context):
    assert context.pangram.check(context.word) == True


@then("error")
def step_impl(context):
    assert_that(context.pangram.check).raises(TypeError).when_called_with(context.word)


@then("empty word")
def step_impl(context):
    assert_that(context.pangram.check).raises(Exception).when_called_with(context.word)

