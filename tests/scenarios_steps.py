from simple_bdd import *

def two_numbers(context: BddContext, number1: int, number2: int):
    context.number1 = number1
    context.number2 = number2

def we_add_them(context: BddContext):
     context.result = context.number1 + context.number2

def we_get_the_expected_result(context: BddContext, result: int):
     assert context.result == result