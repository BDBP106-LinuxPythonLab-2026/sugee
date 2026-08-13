echo $0
name=$1
age=$2

echo 'the first argument is:'$1
echo 'the second argument is:'$2
 

echo 'the number of arguments passed to this script: '$#

echo 'the array/list of arguments passed to this script: '$@
#we can store the arguments in an array by enclosing $@ within ()

listofarg=($@)
#recall elements like any other array

echo ${listofarg[1]}




