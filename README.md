# Overview

This tool intelligently traces a Python program by only showing selected lines of execution.  
We only show conditionals that evaluate to True.  
Within loops, we show the first path and any unique ones thereafter.

## Coverage

![Coverage badge](https://z5267282.github.io/thesis/coverage-badge.svg)

- [Coverage report](https://z5267282.github.io/thesis/htmlcov/index.html)

# Restrictions

Programs are restricted to the following syntax features:

1. Variable assignments
2. Printing
3. Conditionals
4. While loops

# Usage

## Remote

A remote deploy of the tool can be found [here](https://focus-tracker.netlify.app/).

## Docker

The front end and back end have been containerised as Docker images.  
The tool can be run in Docker with the following command.

```sh
docker compose up --build
```

## Local

See the README file in the `backend` and `frontend` folders for manual installation.
