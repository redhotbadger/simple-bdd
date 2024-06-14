import pytest
from simple_bdd import *
from tests.bdd_generic_steps import *

@pytest.mark.xfail(strict=True)
def test_that_when_Given_is_called_and_the_action_fails_then_the_test_fails():
    Given(action_that_fails)

@pytest.mark.xfail(strict=True)
def test_that_when_And_is_called_and_the_action_fails_then_the_test_fails():
    And(action_that_fails)

@pytest.mark.xfail(strict=True)
def test_that_when_When_is_called_and_the_action_fails_then_the_test_fails():
    When(action_that_fails)

@pytest.mark.xfail(strict=True)
def test_that_when_Then_is_called_and_the_action_fails_then_the_test_fails():
    Then(action_that_fails)