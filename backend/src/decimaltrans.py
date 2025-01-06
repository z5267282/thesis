import ast
import os
import re
from decimal import Decimal
from dataframe import DataFrame

class DecimalTransformer(ast.NodeTransformer):
    def visit_Constant(self, node):
        if isinstance(node.value, (int, float)):
            return ast.Call(
                func=ast.Name(id='Decimal', ctx=ast.Load()),
                args=[ast.Constant(value=str(node.value))],
                keywords=[]
            )
        return node

    def visit_Name(self, node):
        return node

def transform_to_decimal(filename : str) -> None:
    """Convert all int and float type variables in the code within the document to Decimal format."""
    filepath : str = os.path.join(os.path.dirname(__file__), filename)
    with open(filepath, 'r') as file:
        code = file.read()
    tree = ast.parse(code)
    transformer = DecimalTransformer()
    tree = transformer.visit(tree)
    import_node = ast.ImportFrom(
        module='decimal',
        names=[ast.alias(name='Decimal', asname=None)],
        level=0
    )
    tree.body.insert(0, import_node) 
    ast.fix_missing_locations(tree)
    with open(filepath, 'w') as file:
        file.write(ast.unparse(tree))
    return

def restore_decimal_to_number(dataframe: DataFrame) -> None:
    """
    Convert all Decimal('x') values in the code attribute of the DataFrame 
    back to their original numerical values.
    """
    decimal_pattern = re.compile(r"Decimal\('([\d.]+)'\)")
    restored_code = []
    for line in dataframe.code:
        restored_line = decimal_pattern.sub(lambda match: match.group(1), line)
        restored_code.append(restored_line)
    dataframe.code = restored_code