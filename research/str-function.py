raw_code = """i = 0
print(i)"""

LEADING_SPACES = 4

code : list[str] = ["def program():"]
code.extend(
    "{}{}".format(" " * LEADING_SPACES, raw)
        for raw in raw_code.split("\n")
)

namespace = {}
source = "\n".join(code)
exec(source, namespace)
prog = namespace["program"]
print(prog)

prog()
