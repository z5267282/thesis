#!/bin/dash

# usage : dash upload.sh <program>
# feed in a user program and trace
# use dash in case there are POSIX issues with bash / zsh has

ERR_CLIENT=1
ERR_TIMEOUT=2

program="$1"
cwd="$(pwd)"
cd /tmp
printf "%s" "$program" > raw.py

dash timeout.sh || exit $ERR_TIMEOUT

# wrap program
sed -E -e 's/^/    /' -e '1i\
def program():' \
raw.py > program.py

# trace
cd "$cwd"
cd ../../backend/src/
python3 main.py
