def safe_read(filename):

    try:
        with open(filename , "r")as file:
          name = file.read()
          return name
    except FileNotFoundError:
        print("File not found, please enter a valid filrname.")
        return None

content1 = safe_read("names.txt")
content2 = safe_read("nonexistent.txt")


print(content1)
print(content2)