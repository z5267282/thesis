import ast

with open("normal.py", "r") as f:
    tree = ast.parse(f.read())

print(ast.dump(tree, indent=2))
