import ast

# program = '''if i == 1: print('1')
# elif i == 2:
#     print('2')
# elif i == 3:
#     print('3')
# else:
#     print('none')'''

# tree = ast.parse(program)
# print(ast.dump(tree, indent=2))

nested = '''
if 1 == 1:
    if 2 == 2:
        if 3 == 3:
            print('yes')
'''

tree = ast.parse(nested)
print(ast.dump(tree, indent=2))
