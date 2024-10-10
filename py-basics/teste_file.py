file = open("1657120497300_rover.obs", "r")
str_file = file.read()

print(str_file.count('5  0\n'))