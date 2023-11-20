#!/bin/bash

#--------------------------------------
# Author: Mubeena Udyavar Kazi
# Course: ECEN 5713 - AESD
#--------------------------------------

case "$1" in
    start)
        echo "Starting postgres and webapp..."
        # Run the docker containers for postgres and webapp
        docker-compose up --build -d
        ;;
    stop)
        echo "Stopping postgres and webapp..."
        docker-compose stop
        ;;
    *)
        echo "Usage: $0 {start|stop}"
        exit 1
        ;;
esac
