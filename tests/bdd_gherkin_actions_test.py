import pytest
from simple_bdd import *
from tests.bdd_generic_steps import *

def test_that_when_Given_is_called_the_action_passed_is_called():
    reset_action_that_passes_calls()
    Given(action_that_passes)
    assert action_that_passes_calls_count() == 1

def test_that_when_And_is_called_the_action_passed_is_called():
    reset_action_that_passes_calls()
    And(action_that_passes)
    assert action_that_passes_calls_count() == 1

def test_that_when_When_is_called_the_action_passed_is_called():
    reset_action_that_passes_calls()
    When(action_that_passes)
    assert action_that_passes_calls_count() == 1

def test_that_when_Then_is_called_the_action_passed_is_called():
    reset_action_that_passes_calls()
    Then(action_that_passes)
    assert action_that_passes_calls_count() == 1
