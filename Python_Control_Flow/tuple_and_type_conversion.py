# Tuple is similar to list but instead of square bracket it is rather in parentheses.
my_tuple = (25, "Hello", 'Ami', False, "Apple")

print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])

# count() used to count occurrences of an element or checks the number of time an element occur in a string.
#my_tuple.count()
print(my_tuple.count("Hello"))

# index() used to find the index of a first occurrence of an element. 
#my_tuple.index()
print(my_tuple.index('Ami'))

# convert an integer to a float
my_integer = 7
my_float = float(my_integer)
print('integer to float:', my_float)

my_float = 4.56
my_integer = int(my_float)
print('float to integer:', my_integer)

my_string = "25"
string_to_integer = int(my_string)
print('string to integer:', string_to_integer)

my_string = ["Hello", "Ami", "How", "Are", "You"]
join_string = " ".join(my_string) 
print('join string:', join_string)

