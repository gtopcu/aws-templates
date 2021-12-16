#!/bin/sh
total=0
for var in "$@"
do
    $total=$total+$var
done
echo $total