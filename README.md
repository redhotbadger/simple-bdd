# simple-bdd
A BDD library for testing python code that puts simplicity over magic features.

BDD testing is a great way to provide structure and context to your tests. It helps facilitate readability and reuse of common functions.
The purpose of this library is to provide a quick and simple way to create BDD style tests in python. It is not intended to generate documentation or to use Gherkin files but rather to help developers in creating simple tests using BDD.

## Installation

### Pip
```
pip install simple-bdd
```

### Poetry
```
poetry add simple-bdd
```

## Usage

### Test Setup
Tests are split into two files the **specs** file and the **steps** file. 

**Specs** files should end with *'_specs_test'*.

**Steps** files should mirror the **specs** file name but with *'_steps'* instead of *'_specs_test'*.

#### Example:

For the files:

- simple_bdd_test.py
- simple_bdd_spec.py

In your **steps** file add a reference to the simple-bdd library.

```python
from bdd import *
```

Then add a reference to the **steps** file in your **specs** file like below:

```python
from simple_bdd_spec import *
```


### Test Creation

Tests are created using basic Gherkin syntax.
You can use the following Gherkin methods:

```python
Given()
When()
Then()
And()
```

To create a test start by creating a method prefixed with *'test_'*.
Inside the method using Gherkin syntax create your test spec. See example below:

#### Example:

```python

def test_that_when_we_do_something_something_is_true():
    Given(something)
    When(we_do_something)
    Then(the_something_is_true)

```

Next in your steps file we need to define the steps for the spec to call.

> [!NOTE]  
> You will need to pass the context object into your method. See [Context](#context) for more details.

```python

def something(context: BddContext):
    context.something = 'something'

def we_do_something(context: BddContext):
     context.result = (context.something == 'something')

def the_something_is_true(context: BddContext):
     assert context.result == True
     
```

### Context

To pass data between steps we use the context object. This allows test steps to remain independent and be reused else where in your testing.

#### Write value

```python

context.something = 'something'

```

#### Read value

```python

print(context.something)

```