#!/bin/bash

function usage()
{
cat << EOF
Usage: $0 <Num of Line> <Awite - in Seconds'>
EOF
}

#check arguments
if [[ $# != 2 ]]; then
 usage
 exit 1
fi

#echo $# $0 $1 $2 $3


#chack if argument is number
num='^[0-9]+$'
if ! [[ $1 =~ $num ]] 
then
   echo "error: Not a number" >&2
   exit 1
fi

if ! [[ $2 =~ $num ]]
then
   echo "error: Not a number" >&2
   exit 1
fi

if ! [ -f speedtest-cli.csv ];
then
	echo "date ,time ,download ,upload" >> ./speedtest-cli.csv
fi

#Running loop to create lines
function write_to_csv()
{
	for ((i = 1; i <= $1; i++ ));
	do
		DATE=`date '+%d.%m.%Y,%H:%M:%S'`
        	Down_Upld=`speedtest-cli --simple | awk '{print $2 }' NR=',' ORS=' ' | awk '{print  $2,$3 }' OFS=","`
        	echo "$DATE,$Down_Upld" >> ./speedtest-cli.csv
        	sleep $2
	done
}

write_to_csv $1 $2
