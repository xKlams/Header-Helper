# Header-Helper
Simple Python and Bash script to update your header file with prototypes of the function in your .c files.

inotify-tools is needed, to install use

        sudo apt-get install inotify-tools

To start just use


    sh start.sh /directory/to/your/.c/files/ /header/file/directory/header.h


This will update your header file every time there is a change in you .c files.

To stop the background process just use

    sh stop.sh

This will stop every check on every folder
