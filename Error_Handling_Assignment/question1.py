try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    
    if denominator == 0:
        print("Error: cannot divide by zero.")
    else:
        result = numerator / denominator
        print("The result is:", result)

except ValueError:
    print("Error: please enter valid integers for both the numerator and the denominator.")
