 #!/bin/bash
 read -p "enter first number" first_number
 read -p "enter second number" second_number

 if [[ $first_number -gt 10 &&  $second_number -gt 10 ]]
 then
    echo "Both numbers are greater than 10."
fi

if [[ $first_number -gt 10 || $second_number -gt 10 ]]
then
   echo "At least one number is greater than 10."
fi

if [[ ! $first_number -gt 10 && ! $second_number -gt 10 ]]
then
   echo "Neither number is greater than 10."
fi                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     