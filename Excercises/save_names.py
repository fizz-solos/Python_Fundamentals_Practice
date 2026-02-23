def save_names(names, filename):
    with open (filename, "w")as file:
        for name in names:
            file.write(name + "\n")
names = ["Faizan", "Ali", "Ahmed"]

save_names(names, "names.txt")