import ast

variables = {"a": "fish", "fish": "dog"}
condition = "a + fish == 'fishing'"

# Parse the condition into an AST
parsed_condition = ast.parse(condition, mode='eval')

# Define a custom visitor to substitute variables
class VariableSubstitutionVisitor(ast.NodeTransformer):
    def __init__(self, variables):
        self.variables = variables

    def visit_Name(self, node):
        if node.id in self.variables:
            return ast.copy_location(ast.parse(repr(self.variables[node.id])).body[0].value, node)
        return node

# Create an instance of the custom visitor and apply it to the parsed AST
substitution_visitor = VariableSubstitutionVisitor(variables)
modified_condition = substitution_visitor.visit(parsed_condition)

# Evaluate the modified AST
print(ast.dump(modified_condition))
result = eval(compile(modified_condition, filename='<ast>', mode='eval'))

print(result)
