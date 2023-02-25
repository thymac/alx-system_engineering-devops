#!/usr/bin/env bash

: "
A Bash script that displays the content of the file /etc/passwd.

Your script should only display:

username
user id
Home directory path for the user
Requirements:

You must use the while loop (for and until are forbidden)
"

while IFS=: read username user_id group_id home_dir
do
    echo "$username:$user_id:$home_dir"
done < /etc/passwd

