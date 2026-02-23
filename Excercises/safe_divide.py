def safe_divide(a, b):
    try:
        result = a/b
        return result
    except ZeroDivisionError:
        print("Error: cannot divide by zero.")
        return None
    except TypeError:
        print("Error: both arguments must be numbers.")
        return None
    
print(safe_divide(10, 2)) 
print(safe_divide(10, 0))
print(safe_divide(10, "a"))
