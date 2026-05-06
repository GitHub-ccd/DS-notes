#!/usr/bin/env sh


for ((i=11;i<21;i++))
do
	name="Sections_"$i
	#ls $name
	items=`ls -d $name/dsc-*/.git`
	for item in $items
	do  
		#rm -r -f $item
		ls $item
	done
done


