import ast
import inspect
import linecache

with open("normal.py", "r") as f:
    tree = ast.parse(f.read())

class MyVisitor(ast.NodeVisitor):
    def __init__(self):
        self.whiles = []

    def generic_visit(self, node):
        if isinstance(node, ast.While):
            self.whiles.append(node)
        ast.NodeVisitor.generic_visit(self, node)

# print(ast.dump(tree, indent=2))
visitor = MyVisitor()
visitor.generic_visit(tree)

for w in visitor.whiles:
    # print(ast.dump(w, indent=2))
    lines, number = inspect.getsourcelines(w)
    print(type(w))
    # for l in linecache.getlines("normal.py")[number : number + len(lines)]:
    #     print(l[:-1])
