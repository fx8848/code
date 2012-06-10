#!/bin/bash 

if grep hello TestFile >/dev/null 
then
	echo "found"
else
	echo "not found"
fi
