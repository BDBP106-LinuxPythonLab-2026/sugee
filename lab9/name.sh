#!/bin/bash


name=$1
course=$2
echo "my name is $1"
echo "my course is $2"

echo $#
echo $@
echo $0

#$0 name of the file
#$# the number of arguments(non empty) passed to this script
#$@ represents all the arguments passed to the script

