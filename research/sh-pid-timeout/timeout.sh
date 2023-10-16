python3 script.py &
pid=$!
sleep 1
# term does not kill
# kill -s TERM $pid
kill -s KILL $pid

