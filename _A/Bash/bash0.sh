#!/bin/sh
#sh bash0.sh 1 2 3

for var in "$*"
do
    echo "$var"
done

echo Input1 is $1