#!/bin/sh
executed=0
while [ "$executed" == 0 ] do :
    if [ $(date +%M) -eq 00 ]; then
        echo "Executing."
        executed=1
        nohup "python3.9 bot.py" &
    fi
    sleep 60
done