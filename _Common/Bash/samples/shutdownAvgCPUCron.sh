#!/bin/bash
#sh bash.sh 1 2 3
#https://stackoverflow.com/questions/610839/how-can-i-programmatically-create-a-new-cron-job
#(crontab -l ; echo "* * * * * wget -O - -q http://www.example.com/cron.php") | crontab -
#(crontab -l ; echo "0 * * * * hupChannel.sh") 2>&1 | grep -v "no crontab" | sort | uniq | crontab -
#(crontab -l ; echo "0 * * * * hupChannel.sh") 2>&1 | grep -v "no crontab" | grep -v hupChannel.sh |  sort | uniq | crontab -

#(crontab -l ; echo "*/1 * * * * if (( $(uptime | tail -c 5 | cut -d. -f1  ) < 2 )); then echo $PATH fi) | crontab -
#(crontab -l ; echo "*/1 * * * * 
#(crontab -l ; echo "*/1 * * * * echo $PATH") 2>&1 | grep -v "no crontab" | sort | uniq | crontab -

(crontab -l ; echo "*/1 * * * * if (( $(uptime | tail -c 5 | cut -d. -f1  ) < 10 )); then sudo shutdown fi") 2>&1 | grep -v "no crontab" | sort | uniq | crontab -

# if (( $(uptime | tail -c 5 | cut -d. -f1  ) < 2 )); then
#      echo "CPUUtilCron - Low usage, shutting down"
#      #sudo shutdown now
# fi


# (crontab -l ; echo "*/1 * * * * \


#     while :
#     do
#     load15M=$(uptime | awk -F'[a-z]:' '{ print $2}'| tail -c 5)
#     threshold=20
#     echo $load15M
#     echo $threshold
#     if (( $(echo "$load15M < $threshold" | bc -l) )); then
#         echo "Low usage, shutting down"
#         #sudo shutdown now
#         break
#     else echo "Instance in usage, will not shut down"
#     fi
# ") | crontab -

# head -n 30 file | tail -n 11
# uptime | head -n 30 | tail -c 5
# uptime | awk '{print substr($0,3,7)}'
# uptime | cut -c 3-10
# uptime | tail -c 5
# uptime | tail -c 5 | cut -d. -f1  
