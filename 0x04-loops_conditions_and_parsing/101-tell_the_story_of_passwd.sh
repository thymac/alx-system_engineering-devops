#!/usr/bin/env bash

: "
A Bash script that displays the content of the file /etc/passwd, using the while loop + IFS.

Format: The user USERNAME is part of the GROUP_ID gang, lives in HOME_DIRECTORY and rides COMMAND/SHELL. USER ID's place is protected by the passcode PASSWORD, more info about the user here: USER ID INFO

Requirements:

You must use the while loop (for and until are forbidden)
"

while IFS=: read -r username password userid groupid info homedir shell
do
	echo "The user $username is part of the $groupid gang, lives in $homedir and rides $shell. $userid's place is protected by the passcode $password, more info about the user here: $info"
done < /etc/passwd

