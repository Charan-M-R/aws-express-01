file_name = input('Enter file name: ')

file_obj = open(file_name, "r+")

str_file = file_obj.read()
print(str_file)

file_obj.close()