def insertion_sort(data_list):
    for i in range(1,len(data_list)):
        temp = data_list[i] 
        j = i-1
        while j >= 0 and data_list[j] > temp:
            data_list[j+1] = data_list[j]
            j -= 1
        data_list[j+1] = temp
myList = [54,26,93,17,77,31,44,55,20]
insertion_sort(myList)
print(myList)

