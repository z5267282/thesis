#!/bin/dash

# see if the program can be run
# preserve stdout for original caller

file=$1

cd /tmp
python3 $file
exit $?
