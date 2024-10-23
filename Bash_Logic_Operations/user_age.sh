#!/bin/bash
echo "Enter your age"
read age
if [ $age -lt 18 ]; then 
  echo "You are a minor."
fi
if [ $age -ge 18 ] && [ $age -le 64 ]; then
  echo "You are an adult."
else
  echo "You are a senior."
fi