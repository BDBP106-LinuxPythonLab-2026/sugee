#!/bin/bash

#getting the username of the logged-in user
logged_in_user= $whoami
#checking is the user is logged in
if [ -n "$logged_in_user" ]; then
	echo "The logged-in user is:$logged_in_user"
else
	echo "user is not logged in"
fi

