import ast

with open("normal.py", "r") as f:
    tree = ast.parse(f.read())

class MyVisitor(ast.NodeVisitor):
    def generic_visit(self, node):
        print(f'Nodetype: {type(node).__name__:{16}} {node}')
        ast.NodeVisitor.generic_visit(self, node)

# print(ast.dump(tree, indent=2))
visitor = MyVisitor()
visitor.generic_visit(tree)
