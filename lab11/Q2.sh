#!bin/bash

if [ -e pineapple ];then
	echo "file exists"
else
	echo "file does not exist"
fi


if [ -s pineapple ];then
	echo "file has contents"
else
	echo "file does not have contents"
fi

if [ -f pineapple ];then
	echo "it is a file"
else
	echo "it is a directory"
fi

