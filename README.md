# Overview
This tool intelligently traces a Python program by only showing selected lines of execution.
We only show conditionals that evaluate to True.
Within loops, we show the first path and any unique ones thereafter.
# Restrictions
Programs are restricted to the following syntax features:
1. Variable assignments
2. Printing
3. Conditionals
4. While loops
