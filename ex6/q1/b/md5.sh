#!/bin/bash

#Checks whether the command was executed properly
function usage()
{
cat << EOF
 Usage: ${0} <Num of Line> <Awite in sec'>
EOF
}

if [[ $# != 1 ]]; then
 usage
 exit 1
fi

#check if the argument is directory
if [[ ! -d $1 ]]; then
 echo "$1 does not appear to be a directory"
 exit 1
fi

find $1 -type f | xargs md5sum | awk '{print NR "," $2 "," $1}' >> ./md5sum.csv

#Assigning arguments
#num=1;
#file_list=`find $1 -type f`

#for file in $file_list; 
#do

#	md5=`md5sum $file | awk {'print $1'}`
#	echo $num,./$(basename $file),$md5 >> ./md5sum.csv
#	num=$((num+1))
#done
