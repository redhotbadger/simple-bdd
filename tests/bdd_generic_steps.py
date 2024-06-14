action_that_passes_calls = 0

def reset_action_that_passes_calls():
    global action_that_passes_calls
    action_that_passes_calls = 0

def action_that_passes(context: dict):
    global action_that_passes_calls
    action_that_passes_calls += 1

def action_that_passes_calls_count():
    global action_that_passes_calls
    return action_that_passes_calls

def action_that_fails(context: dict):
    assert False

def action_that_passes_with_context(context: dict):
    context.value.append('action_that_passes_with_context_result')