#!/bin/bash
number=$1
if [ $((number%2)) -eq 0 ]
then
  echo "The number $1 is even"
else
  echo "The number $1 is odd"
fi