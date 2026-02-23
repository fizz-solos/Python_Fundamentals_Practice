numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squared_numbers = [item**2 for item in numbers if item % 2 == 0]

print (f"Squared Even numbers are {squared_numbers}")