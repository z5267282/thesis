def evaluate(expression : str, variables : dict[str, str]):
    """For now, we only support 1 variable subsitution""" 
    for name, value in variables.items():
        if name in expression:
            return expression.replace(name, str(value))
    return expression
