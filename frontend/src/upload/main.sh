#!/bin/dash

# feed in a user program and trace
# use dash in case there are POSIX issues with bash / zsh has

timeout_file=$1
timeout_secds=$2
err_timeout=$3
err_client=$4

dash timeout.sh $timeout_file $timeout_secs || exit $err_timeout

# TODO: wrap program

# trace
cd "$cwd"
cd ../../backend/src/
python3 main.py