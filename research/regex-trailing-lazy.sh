#!/bin/dash

# match will not occur lazily
printf 'fishing : x :             stuff!' | grep -E -o ':.*?$' 

printf 'fishing : x :             stuff!' | grep -E -o ':.[^:]*$' 
