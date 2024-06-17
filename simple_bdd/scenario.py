import collections.abc
import simple_bdd.bdd as bdd
from simple_bdd.bddContext import BddContext
from inspect import signature

class WithScenarios:
    def __init__(self, params, method):

        if isinstance(params, collections.abc.Sequence) != True:
            raise TypeError('Parameter value needs to be an array of objects.') 

        method_sig = signature(method)

        method_params_length = len(method_sig.parameters)

        index = 0
        for param in params:
            param_params_length = len(param)
            if(method_params_length != param_params_length):
                raise TypeError(f'Incorrect number of parameters passed to test. Expected: {method_params_length} but got: {param_params_length}.') 


        method_params = list(method_sig.parameters.values())
        for param in params:
            index = 0
            for key, value in param.items():
                method_param = method_params[index]

                if(method_param.name != key):
                    raise TypeError(f'Parameter is using the wrong name. Expected: {method_param.name} but got: {key}.') 
                index = index + 1


        self.params = params
        self.method = method

    def RunTest(self):
        bdd.context = BddContext()
        for param in self.params:
            self.method(**param)