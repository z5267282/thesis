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

# Environments

Environment variable `REACT_APP_HOST` controls configuration settings about the application.
It can have two possible values:
|value|implications|
|-|-|
|`LOCAL`| The app is configured to run locally|
|`REMOTE`| The app is configured to run on pythonanywhere at this [server](https://z5267282.pythonanywhere.com/)|
If the environment variable is not set, then `REMOTE` is used.
