#!/bin/bash
if [ "$1" != "" ]; then
    mosquitto -p $1
else
    mosquitto -p 3000
fi
