#!/bin/bash
#sh bash.sh 1 2 3
while :
do
  load15M=$(uptime | awk -F'[a-z]:' '{ print $2}'| tail -c 5)
  threshold=20
  echo $load15M
  echo $threshold
  if (( $(echo "$load15M < $threshold" | bc -l) )); then
    echo "Low usage, shutting down"
    sudo shutdown now
    break
  else echo "Instance in usage, will not shut down"
  fi
  sleep 60
done
