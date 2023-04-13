#!/bin/bash

case ${1} in
        "start")
        nginx-prometheus-exporter -nginx.scrape-uri=http://127.0.0.1:80/status --web.listen-address ":9001" >> /home/weichih/exporter/log/local:80 2>&1 &
        nginx-prometheus-exporter -nginx.scrape-uri=http://192.168.56.104:8080/server-status --web.listen-address ":9002" >> /home/weichih/exporter/log/104:8080 2>&1 &
        nginx-prometheus-exporter -nginx.scrape-uri=http://192.168.56.102:80/status --web.listen-address ":9003" >> /home/weichih/exporter/log/102:80 2>&1 &

        ;;
        "restart")

        ;;
        "stop")
        echo "HI"
        ;;
        *)
        echo "錯的參數"
        ;;
esac