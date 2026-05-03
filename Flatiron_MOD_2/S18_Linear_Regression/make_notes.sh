#!/usr/bin/env sh

#cnt=1
while read path
do
  #echo $cnt
  #echo $l
  cd $path

  # syntax jupyter nbconvert --execute --to pdf notebook.ipynb
  # jupyter nbconvert --execute --to html notebook.ipynb
  jupyter nbconvert -y --allow-errors --execute --to html index.ipynb

  ls index.html
  cp ../html2pdf.py .
  python html2pdf.py
  ls index.pdf

  cd ..
  #cnt=$((cnt + 1))
done < note_list.txt
