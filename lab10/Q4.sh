
#!bin/bash

echo 'enter a number'
read number
if [ $number -gt 0 ];then
	echo "$number is positive number"
elif [ $number  -lt 0 ];then
	echo "$number  is negative number"
else
	echo "the number is 0"
fi

