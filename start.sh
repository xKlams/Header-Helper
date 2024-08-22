#!/bin/bash

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
cp "$1""$2" ./headers_backup/
path_first_char="${1:0:1}"
header_first_char="${2:0:1}"
HEADER_DIR="$2"
if [ "header_first_char" != "/" ]; then
	HEADER_DIR="/$2"
fi
DIRECTORY="$1"
if [ "$first_char" != "/" ]; then
	DIRECTORY="$SCRIPT_DIR/$1"
fi
echo "sh monitor.sh $DIRECTORY $HEADER_DIR > /dev/null 2 >&1 &"
sh monitor.sh $DIRECTORY $HEADER_DIR > /dev/null 2>&1 &
