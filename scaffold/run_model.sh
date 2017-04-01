#!/bin/bash

listFloats=0.0
for i in {0..4}
do
	aux=$(printf "0.%03d%02d" $(( $RANDOM % 1000 )) $(( $RANDOM % 100)))
	if [ ${i} -eq 0 ]
	then
		listFloats=${aux}
		#printf ${aux} > randomFloats.txt
	else 
		listFloats="${listFloats} ${aux}"
		#printf ${aux} >> randomFloats.txt
	fi
done

printf "%s " ${listFloats}
printf "\n"
