#!/bin/bash
#sh bash.sh 1 2 3

num=$1
a=1
b=2
c=$((a+b))
c=$((c+1))
echo $c

for var in "$*"
do
    echo "$var"
done

for ((i=1; i<=10; i++)); 
do
    num=$((num+i))
    c=$((c+1))
done


while true; do echo; done

echo "$num"



