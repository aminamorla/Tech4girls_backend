is_student = True      #change to false to test ii.3.
is_employed = True     #change to false to test ii.2.
if is_student and is_employed:
    print("You are a working student.")

elif is_student and not is_employed:
    print("You are a student.")
elif not is_student and is_employed:
    print("You are employed but not a student.")



#iii.
age = int(input("Enter your age "))
if age >= 18:
   license = input("Do you have a driver's license? (yes/no):")
   if license == 'yes':
       print("You are allowed to drive.")
   else:
       print("You need a driver's license to drive.")
else:
   
   print("You are not old enough to drive.")
