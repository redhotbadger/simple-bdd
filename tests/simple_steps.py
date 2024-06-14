from simple_bdd import *

def something(context: BddContext):
    context.something = 'something'

def we_do_something(context: BddContext):
     context.result = (context.something == 'something')

def the_something_is_true(context: BddContext):
     assert context.result == True