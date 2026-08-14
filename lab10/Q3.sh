
#!bin/bash
echo "enter your filename"
read filename

if [ -f "$filename" ];then
	if [ -x "$filename" ];then
		echo "file exists & is executable"
	 else
		echo "file exists & is not executable"
	fi
echo 'the file exists'	
exit 200
echo $?

else
	echo "file does not exist"
	exit 201
        echo $?

fi





