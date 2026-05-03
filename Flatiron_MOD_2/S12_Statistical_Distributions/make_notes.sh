#!/usr/bin/env sh

#cnt=1
while read l
do
	#echo $cnt
	#echo $l
	cd $l
	ls index.html
	cp ../html2pdf.py .
	python html2pdf.py
	ls index.pdf
	cd ..
	#cnt=$((cnt + 1))
done < note_list.txt
