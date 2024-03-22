#!/bin/bash

# Update owner, group and permissions of all folders under /home/cr-study-2024
# except for the 'common' folder. The owner is the name of the folder, the group
# is 'cr-team' and the permissions are 770.

cd /home/cr-study-2024 || exit
for folder in *
do
    folder=${folder%/}
    if [ "$folder" != "common" ]
    then
        chown -R "$folder":cr-team "$folder"
        chmod -R 770 "$folder"
    fi
done