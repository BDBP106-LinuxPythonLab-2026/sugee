#!/bin/bash

function filedir {
	echo "enter a filename"
	read filename
	if [ -e "$filename" ];then
		echo "file exists"
		ls $filename
	else
		mkdir newdirectory
		echo "newdirectory is created"
	fi
}
filedir 
