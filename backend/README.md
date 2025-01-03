# Running

The backend can be started via

```sh
start
```

. Note this starts a virtual environment.

# Test Linting

`lint/` contains shell scripts which perform linting checks on test files.

| file           | check                                                                                                                                             |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| `func-in-file` | Check a test has a primary function named after its filename. Not applicable for files which test multiple functions from a module                |
| `prefix`       | find all common prefixes in test names. Common prefixes are an indicator of an unnecessarily long filename (eg. the directory is in the filename) |
