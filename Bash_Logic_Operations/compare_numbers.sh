#!/bin/bash
echo "Enter the first numbe:"
read num1
echo "Enter the second number:"
read num2

if [ $num1 -gt $num2 ]; then
  echo "$1 is greater than $2"
if [ $num1 -lt $num2 ]; then
  echo "$num2 is greater than $num1"
else
  echo "The numbers are equal"
fi