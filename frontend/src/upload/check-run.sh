#!/bin/dash

# see if the program can be run
# preserve stdout for original caller

# we pass in the program as a string to avoid relying on temporary files
program="$1"

cd /tmp
printf '%s' "$program" > 
