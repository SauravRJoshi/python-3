def insertion_sort(input_list):
    for i in range(1, len(input_list)):
        n = input_list[i]
        pos = i
        while pos > 0 and input_list[pos-1] > n:
            input_list[pos] = input_list[pos-1]
            pos -= 1
        input_list[pos] = n
    return input_list

input_list = [1000,1111,5000,2000,25000,6060,121,1130,10000]
print("pre sort: ",input_list)
print("post sort: ",insertion_sort(input_list))