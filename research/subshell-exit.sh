#!/bin/dash

# check if running a subshell command preserves exit status

$(exit 42)
echo $?
