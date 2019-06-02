#!/bin/bash


function usage()
{
cat << EOF
Usage: ${0} <Ext> <Path>'
EOF
}

#check arguments
if [[ $# != 2 ]]; 
then
 usage
 exit 1
fi

#check if the fitsr argument is directory
if [[ ! -d $2 ]]; 
then
 usage
 exit 1
fi

#Running loop on folder to change to other ext
function recursive_change_ext()
{
	for fileName in $(ls $2);
	do
		filename=$(basename -- "$fileName")
		extension="${filename##*.}"
		filename="${filename%.*}"
		if [ -d $2/$fileName ]; 
		then
			echo "$2/$fileName is a dir"
			recursive_change_ext $1 $2/$fileName
			continue
		fi

		if [ "$extension" != "$1" ]
        	then
			echo Change from "$2/$fileName" to "$2/$fileName.$1"
			mv "$2/$fileName" "$2/$filename.$1"
		else
        	        echo "The file - ${fileName} already has that extension of $1"
	        fi

	done
}

recursive_change_ext $1 $2

