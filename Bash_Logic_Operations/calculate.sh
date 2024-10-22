#!/bin/bash
number=$1
number=$2
number=$3

sum=$(($1 + $2))
product=$(( $sum * $3))
echo "The sum of $1 and $2 is: $sum"
echo "Multiplying the sum by $3 gives: $product"