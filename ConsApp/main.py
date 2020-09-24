from read_info import ReadFile
from write_info import WriteFile
from edit_info import Edit_file

read_file = ReadFile()
write_file = WriteFile()
edit_file = Edit_file()

while True:
    user_input = int(input("give your input "))
    if user_input == 1:
            print(read_file.read_course_info())
    elif user_input == 2:
            print(read_file.read_st_info())
    elif user_input == 3:
            print("To edit info provide the following parameters :")
            roll = input("Enter a roll number ")
            val = input("Enter 1 for name, 2 for address, 3 for number ")
            user_input = input("Enter the value ")
            edit_file.edit_info(roll,user_input,val)
    elif user_input == 4:
            val = str(input("To delete input the roll number "))
            write_file.delete_detail(val)
    elif user_input == 0:
        break