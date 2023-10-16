python3 script.py &
pid=$!
sleep 1
kill -s TERM $pid

