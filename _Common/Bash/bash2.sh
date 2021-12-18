#!/bin/bash
#sh bash.sh 1 2 3

# [A-Z]:        Uppercase characters through A to Z
# [^a-zA-Z0-9]: Aynthing except these

count=0
for var in "$@": 
do
    echo $count $var
    if [[ $var =~ [A-Z] ]]
    then
        echo "match!"
        ((count++))
        count=$((count+1))
    fi
done
echo $count
