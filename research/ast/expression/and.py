import ast
expression = "x % 3 == 0 and x % 4 == 0"
tree = ast.parse(expression)
print(ast.dump(tree, indent=2))

