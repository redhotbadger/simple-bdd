import pytest
from simple_bdd.bddContext import BddContext

context = BddContext()

@pytest.fixture(autouse=True)
def before_each():
    global context
    context = BddContext()

def Given(action, *args):
    action(context, *args)

def When(action, *args):
    action(context, *args)

def Then(action, *args):
    action(context, *args)

def And(action, *args):
    action(context, *args)