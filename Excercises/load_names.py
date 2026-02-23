def load_names(filename):
    with open(filename, "r")as file:
        names = file.readlines()
        clean_names=[]
        for name in names:
            clean_names.append(name.strip())
    
    for i in range (len(clean_names)):
        print(f"{i+1}. {clean_names[i]}")

    return len(clean_names)

count = load_names("names.txt")
print(f"total names: {count}")

    
