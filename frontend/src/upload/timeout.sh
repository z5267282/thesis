#!/bin/dash

file=$1
timeout_secs=$2

cd /tmp
python3 $file & > /dev/null
pid=$!
sleep $timeout_secs
if ps -p $pid > /dev/null
then
    kill -s TERM $pid
    exit 1
fi
exit 0
