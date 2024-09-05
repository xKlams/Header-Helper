#!/bin/bash

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
cp "$1""$2" ./headers_backup/
first_arg=$1
path_first_char="${first_arg:0:1}"
second_arg=$2
header_first_char="${second_arg:0:1}"
HEADER_DIR="$2"
if [ "$header_first_char" != "/" ]; then
	HEADER_DIR="/$2"
fi
DIRECTORY="$1"
if [ "$path_first_char" != "/" ]; then
	DIRECTORY="$SCRIPT_DIR/$1"
fi
sh monitor.sh $DIRECTORY $HEADER_DIR > /dev/null 2>&1 &
