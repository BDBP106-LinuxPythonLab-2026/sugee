
#!bin/bash
echo "enter your filename"
read filename

if [ -f "$filename" ];then
	if [ -x "$filename" ];then
		echo "file exists & is executable"
	 else
		echo "file exists & is not executable"
	fi

else
	echo "file does not exist"
fi



