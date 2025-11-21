# Overview

This tool intelligently traces a Python program by only showing selected lines of execution.
We only show conditionals that evaluate to True.
Within loops, we show the first path and any unique ones thereafter.

## Coverage

![Coverage badge](https://z5267282.github.io/thesis/coverage-badge.svg)
[Coverage report](https://z5267282.github.io/thesis/htmlcov/index.html)

# Restrictions

Programs are restricted to the following syntax features:

1. Variable assignments
2. Printing
3. Conditionals
4. While loops

# Usage

## Remote

A remote deploy of the tool can be found [here](https://focus-tracker.netlify.app/).

## Local Set Up

It is expected that the following utilities are installed on your system

```
python3
npm
```

. Simply run

```sh
./setup
```

to install all necessary dependencies.

For the front end and back end, navigate to the `frontend` and `backend` folders respectively in separate terminals, and run the following commands to start the tool

| component | command     |
| --------- | ----------- |
| frontend  | `npm start` |
| backend   | `start`     |

.
