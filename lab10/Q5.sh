#!bin/bash

echo  "enter a range"
read n
if [ $n -gt 100 ];then
	echo "$n is greater than 100"

elif [ $n -ge 90 ];then
	echo "$n is grade "A"" 
elif [ $n -ge 80 ];then
	echo "$n is grade "B""
elif [ $n -ge 70 ];then
	echo "$n is grade "C""
else 
	echo "fail"

fi

