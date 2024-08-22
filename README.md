# Header_Updater
Simple Python and Bash script to update your header file with prototypes of the function in your .c files.

inotify-tools is needed, to install use

        sudo apt-get install inotify-tools
        sudo dnf install ionotify-tools

To start just use


        sh start.sh /directory/to/your/project/ /relative/header/directory/header/file.h

For example if my project is in "/home/user/projects/test/" and my header file is in "/home/user/projects/test/headers/file.h" i should run

        sh start.sh ~/projects/test/ /headers/file.h

This will update your header file every time there is a change in you .c files.

To stop the background process just use

        sh stop.sh

This will stop every check on every folder
