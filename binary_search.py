def binarySearch(input_list, input_num):
    first = 0
    last = len(input_list)-1
    found = False
    index_location = 0

    while first<=last and not found:
        midpoint = (first + last)//2
        if input_list[midpoint] == input_num:
            found = True
            index_location = input_list.index(input_num)
        else:
            if input_num < input_list[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    if found == True:
        return "Found at ",index_location
    else:
        return "Not found"

input_list = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print("Sample list : ",input_list)
input_num = int(input("Enter you number to search : "))
print(binarySearch(input_list,input_num))