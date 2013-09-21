#!/bin/bash

os=`uname`

if [ "$#" -eq 1 ]
then
	echo "Clean adobe's metadata";
	for file in $(find $1  -name "*.html");
	do
		# sed -i -e "s/chaine1/chaine2/g" "$file"
		sed -i -e "/<meta name=\"generator\" content=\"Adobe Photoshop Lightroom\" >/d" "$file";

		sed -i -e "s/,adobe,photoshop,lightroom//g" "$file";

		# if MAC OSX
		if [ "$os" == "Darwin" ] 
		then
		  rm "$file-e"
		fi
		

		echo "File $file is cleaned.";
	done
else
	echo "Wrong parameter";
fi