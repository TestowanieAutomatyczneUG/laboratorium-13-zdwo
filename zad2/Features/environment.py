from zad2.IsPangram import Pangram

def before_scenario(context, scenario):
    context.pangram = Pangram()

def after_scenario(context, scenario):
    context.pangram = None