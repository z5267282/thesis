from typing import Any

def evaluate(expression : str, variables : dict[str, Any]):
    """For now, we only support 1 variable subsitution""" 
    result = expression
    for name, value in variables.items():
        result = result.replace(name, str(value))
    return result
