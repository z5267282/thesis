#!/bin/dash

# feed in a user program and trace
# use dash in case there are POSIX issues with bash / zsh has

timeout_file=$1
timeout_secds=$2
raw_file=$3
err_timeout=$4
err_client=$5

dash timeout.sh $timeout_file $timeout_secs || exit $err_timeout
dash sanity-run.sh $raw_file || exit $err_client


# trace
cd "$cwd"
cd ../../backend/src/
python3 main.py
