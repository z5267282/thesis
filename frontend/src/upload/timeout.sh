#!/bin/dash

program="$1"

TIMEOUT_SECS=1

cd /tmp
python3 raw.py > /dev/null 2>&1 &
pid=$!
sleep $TIMEOUT_SECS
ps -p $pid > /dev/null && exit 1
exit 0
