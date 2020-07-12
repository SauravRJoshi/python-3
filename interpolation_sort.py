
def interpolationSearch(sample_list, length_of_list, x):  
    lower_value = 0
    higher_value = (length_of_list - 1) 
    
    while lower_value <= higher_value and x >= sample_list[lower_value] and x <= sample_list[higher_value]: 
        if lower_value == higher_value: 
            if sample_list[lower_value] == x:  
                return lower_value; 
            return -1; 
           
        pos  = lower_value + int(((float(higher_value - lower_value) / 
            ( sample_list[higher_value] - sample_list[lower_value])) * ( x - sample_list[lower_value]))) 
  
        if sample_list[pos] == x: 
            return pos 
 
        if sample_list[pos] < x: 
            lower_value = pos + 1; 
 
        else: 
            higher_value = pos - 1; 

    return -1
  

sample_list = [10, 12, 13, 16, 18, 19, 20, 21, 
                22, 23, 24, 33, 35, 42, 47] 
length_of_list = len(sample_list) 
print("The sample list is : ",sample_list)
x = int(input("Enter the number to search : "))  
index = interpolationSearch(sample_list, length_of_list, x) 
  
if index != -1: 
    print("Your number was found at index",index)
else: 
    print("Your number was not found")