#!/bin/dash

TIMEOUT_SECS=1

program="$1"

cd /tmp
# gracefully handle timeout using a TERM signal handler
tee raw.py << EOF > /dev/null
from signal import SIGTERM, signal
import sys
signal(
    SIGTERM, timeout=lambda signum, frame: sys.exit(1)
)
$program
EOF

python3 raw.py & > /dev/null
pid=$!
sleep $TIMEOUT_SECS
if ps -p $pid > /dev/null
then
    kill -s TERM $pid
    exit 1
fi
exit 0
