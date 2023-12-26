from typing import Any

def evaluate(expression : str, variables : dict[str, Any]) -> str:
    """A simple string replacement algorithm; will not evaluate expressions""" 
    result : str = expression
    for name, value in variables.items():
        result = result.replace(name, str(value))
    return result
