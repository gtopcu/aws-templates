#!/bin/bash

num=$1

for ((i=1; i<=10; i++)); do
    num=$((num+i))
done

while true; do echo; done

echo "$num"



