from .bdd_scenario_steps import *

def test_that_when_we_have_a_collection_of_params_and_a_test_method_then_the_test_steps_are_all_called():
    Given(a_scenario_params)
    And(a_scenario_method)
    When(we_call_scenario_test_with_params)
    Then(all_the_methods_are_called_with_the_params)

def test_that_when_we_have_a_none_array_params_and_a_test_method_then_when_we_build_the_scenario_it_fails():
    Given(a_scenario_params_that_is_not_an_array)
    And(a_scenario_method)
    When(we_call_scenario_test_with_params)
    Then(it_failed_with_the_error_explaining_the_params_are_incorrect)

def test_that_when_we_have_an_array_of_incorrect_number_of_params_and_a_test_method_then_when_we_build_the_scenario_it_fails():
    Given(a_scenario_params_that_is_an_array_of_incorrect_number_of_params)
    And(a_scenario_method)
    When(we_call_scenario_test_with_params)
    Then(it_failed_with_the_error_explaining_the_params_are_not_the_correct_number_of_params)

def test_that_when_we_have_an_array_of_params_with_the_wrong_names_and_a_test_method_then_when_we_build_the_scenario_it_fails():
    Given(a_scenario_params_that_is_an_array_of_params_with_the_wrong_names)
    And(a_scenario_method)
    When(we_call_scenario_test_with_params)
    Then(it_failed_with_the_error_explaining_the_params_are_not_using_the_right_names)