def partiton(input_list, left, right):
	i = left + 1 
	pivot = input_list[left]
	for j in range(left+1, right+1): 
		if (input_list[j] < pivot):
			input_list[i], input_list[j] = input_list[j], input_list[i] 
			i = i+1
	pos = i - 1
	input_list[left], input_list[pos] =  input_list[pos], input_list[left]
	return pos



def quickSort(input_list, left, right):
	if(left <  right):
		pivot = partiton(input_list, left, right)
		quickSort(input_list, left, pivot-1)
		quickSort(input_list, pivot+1, right)


if __name__ == '__main__':
	input_list = [1000,2000,1500,1420,5000,3000,45000]
	print("Pre Sort :",input_list)
	quickSort(input_list ,0 , len(input_list)-1)
	print("Post Sort :",input_list)