from simple_bdd import *

calls = []

def a_scenario_params(context: BddContext):
    context.params = [
        {'val1': 'test1', 'val2': 1},
        {'val1': 'test2', 'val2': 2},
        {'val1': 'test3', 'val2': 3},
    ]

def a_scenario_params_that_is_not_an_array(context: BddContext):
    context.params = {'val3': 'test3', 'val2': 3}

def a_scenario_params_that_is_an_array_of_incorrect_number_of_params(context: BddContext):
    context.params = [
        {'val1': 'test1', 'val2': 1, 'val3': 'error'},
        {'val1': 'test2', 'val2': 2, 'val3': 'error'},
        {'val1': 'test3', 'val2': 3, 'val3': 'error'},
    ]

def a_scenario_params_that_is_an_array_of_params_with_the_wrong_names(context: BddContext):
    context.params = [
        {'val3': 'test1', 'val2': 1},
        {'val3': 'test2', 'val2': 2},
        {'val3': 'test3', 'val2': 3},
    ]

def a_scenario_method(context: BddContext):
    def scenario_method(val1: str, val2: int):
        calls.append([val1, val2])

    context.method = scenario_method

def we_call_scenario_test_with_params(context: BddContext):
    try:
        scenario_tester = WithScenarios(context.params, context.method)
        scenario_tester.RunTest()
    except Exception as e:
        context.error = repr(e)

def all_the_methods_are_called_with_the_params(context: BddContext):
    assert calls[0] == ['test1', 1]
    assert calls[1] == ['test2', 2]
    assert calls[2] == ['test3', 3]

def it_failed_with_the_error_explaining_the_params_are_incorrect(context: BddContext):
    assert context.error == 'TypeError(\'Parameter value needs to be an array of objects.\')'

def it_failed_with_the_error_explaining_the_params_are_not_the_correct_number_of_params(context: BddContext):
    assert context.error == 'TypeError(\'Incorrect number of parameters passed to test. Expected: 2 but got: 3.\')'

def it_failed_with_the_error_explaining_the_params_are_not_using_the_right_names(context: BddContext):
    assert context.error == 'TypeError(\'Parameter is using the wrong name. Expected: val1 but got: val3.\')'