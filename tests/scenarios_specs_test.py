from .scenarios_steps import *

def test_that_when_we_have_some_scenarios_we_can_call_the_method_with_them():
    scenarios = [
        {'number1': 1, 'number2': 1, 'result': 2},
        {'number1': 1, 'number2': 2, 'result': 3},
        {'number1': 1, 'number2': 3, 'result': 4},
    ]

    def method(number1: int, number2: int, result: int):
        Given(two_numbers, number1, number2)
        When(we_add_them)
        Then(we_get_the_expected_result, result)

    WithScenarios(scenarios, method).RunTest()