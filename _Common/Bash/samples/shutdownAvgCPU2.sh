#!/bin/bash
#sh bash.sh 1 2 3
#does not work!
while :
do
  load5M=$(uptime | awk -F'[a-z]:' '{ print $2}' | cut -d, -f1)
  threshold=20
  echo $load5M
  if (( $(echo "$load5M < $threshold" | bc -l) )); then
    sudo shutdown now
    break
  fi
  sleep 5
done
