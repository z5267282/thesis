import ast

expression = "x == 2"
tree = ast.parse(expression)
print(ast.dump(tree, indent=2))
print(type(tree))

