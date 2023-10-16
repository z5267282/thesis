#!/bin/dash

# usage : dash upload.sh <program>

# feed in a user program and trace
# use dash in case there are POSIX issues with bash / zsh has

ERR_CLIENT=1
ERR_TIMEOUT=2

TIMEOUT_SECS=1

program="$1"
cwd="$(pwd)"

# run program
cd /tmp
printf "%s" "$program" > raw.py
output=$(mktemp)
trap 'rm -rf $output' EXIT
# we want to preserve stderr as well
python3 raw.py > $output 2>&1 &
status=$?
pid=$!
sleep $TIMEOUT_SECS
if [ $status -ne 0 ]
then
    cat $output
    exit $ERR_CLIENT
fi
ps -p $pid > /dev/null && exit $TIMEOUT_SECS

# wrap program
sed -E -e 's/^/    /' -e '1i\
def program():' raw.py > program.py

# trace
cd "$cwd"
