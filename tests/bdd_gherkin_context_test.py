import pytest
import simple_bdd
from simple_bdd import *
from tests.bdd_generic_steps import *

def reset_context():
    simple_bdd.bdd.context.value = []

def test_that_when_Given_is_called_with_an_action_that_updates_the_context_then_the_context_is_updated_with_that_actions_value():
    reset_context()
    Given(action_that_passes_with_context)
    assert simple_bdd.bdd.context.value[0] == 'action_that_passes_with_context_result'

def test_that_when_And_is_called_with_an_action_that_updates_the_context_then_the_context_is_updated_with_that_actions_value():
    reset_context()
    And(action_that_passes_with_context)
    assert simple_bdd.bdd.context.value[0] == 'action_that_passes_with_context_result'

def test_that_when_When_is_called_with_an_action_that_updates_the_context_then_the_context_is_updated_with_that_actions_value():
    reset_context()
    When(action_that_passes_with_context)
    assert simple_bdd.bdd.context.value[0] == 'action_that_passes_with_context_result'

def test_that_when_Then_is_called_with_an_action_that_updates_the_context_then_the_context_is_updated_with_that_actions_value():
    reset_context()
    Then(action_that_passes_with_context)
    assert simple_bdd.bdd.context.value[0] == 'action_that_passes_with_context_result'

def test_that_when_both_Given_and_Then_are_called_with_an_action_that_updates_the_context_then_both_the_values_are_in_the_context():
    reset_context()
    Given(action_that_passes_with_context)
    Then(action_that_passes_with_context)
    assert simple_bdd.bdd.context.value[0] == 'action_that_passes_with_context_result'
    assert simple_bdd.bdd.context.value[1] == 'action_that_passes_with_context_result'

@pytest.mark.run(order=1)
def test_first_test():
    simple_bdd.bdd.context.value = 'value'

@pytest.mark.run(order=2)
def test_that_when_the_context_has_a_value_it_is_cleared_before_the_test():
    assert hasattr(simple_bdd.bdd.context, 'value') == False