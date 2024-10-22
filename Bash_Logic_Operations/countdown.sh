#!/bin/bash
echo "Enter a number"
read number
while [[ $number -gt 4 ]]
do 
   echo $number
   number=$((number-1))
done
   echo "Countdown complete!"
