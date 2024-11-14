data = {"name": "Amina", "age": 15, "country": "Germany"}
key = input("Enter the key you want to look up: ")
 
try: 
    print("value:", data[key])
except KeyError:
    print(f"Error: The key '{key}' was not found in the dictionary.")