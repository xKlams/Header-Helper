#!/bin/bash

cp "$1""$2" ./headers_backup/
sh monitor.sh $1 $2 > /dev/null 2>&1 &
