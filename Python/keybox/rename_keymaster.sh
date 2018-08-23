#!/bin/bash

function scandir()
{
		cd $1
		rename 's/ /_/g' *
		cd -
		
    OLDINF=$IFS
    IFS=$'\n\n'

    for file in `ls $1`; do
        full_path=$1/$file
        full_path=${full_path#./}
        name=${full_path##*/}
        path=${full_path%/*}
        #echo "full_path=$full_path path=$path name=$name"
        
        new_name=`sed -n '/DeviceID="/p' ${full_path}`
        new_name=${new_name##*DeviceID\=\"}
        new_name=${new_name%%\"><Key*}
        #echo "new_name=$new_name"
        
        #if [ x"$name" != x"strings.xml" ]; then
            #echo "name=$name"
            mkdir -p ./rename_keymaster
            cp $full_path ./rename_keymaster/$new_name.xml
        #fi
    done

    IFS=$OLDINF
}

scandir $1
