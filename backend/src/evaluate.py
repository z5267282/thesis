from typing import Any

def evaluate(expression : str, variables : dict[str, Any]):
    """A simple string replacement algorithm; will not evaluate expressions""" 
    result = expression
    for name, value in variables.items():
        result = result.replace(name, str(value))
    return result
