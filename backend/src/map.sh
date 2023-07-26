i=0
while [ $i -lt 12 ]
do
    n=$(sed -n $((i + 1))p line-nums.txt)
    echo "assert filtered[$i].line_no == $((n + 8))"
    i=$((i + 1))
done
