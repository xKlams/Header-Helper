#!/bin/bash

DIRECTORY_TO_MONITOR=$1
HEADER_FILE=$2
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

inotifywait -m -e modify,create,delete "$DIRECTORY_TO_MONITOR" |
while read path action file; do
    # Perform your action here
    if [ "/$file" != "$HEADER_FILE" ]; then
    	python3 "$SCRIPT_DIR"/header_updater.py $DIRECTORY_TO_MONITOR $HEADER_FILE
    fi
done
