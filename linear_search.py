input_list = []
input_num = int(input("Enter how many elements you want:"))
print('Enter numbers in array: ')
for i in range(0, input_num):
    n = int(input("your input :"))
    input_list.append(n)
element_to_find = int(input("Element to find :"))
element_found = False    
for i in input_list:
    if i==element_to_find:
        element_found = True
        print("The number was found at the index ",input_list.index(i))
if not element_found:
    print("The number was not found !")