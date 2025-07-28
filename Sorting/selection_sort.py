def selction_Sort(data_list):
    n = len(data_list)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if data_list[j] < data_list[min_index]:
                min_index = j
        data_list[i],data_list[min_index] = data_list[min_index],data_list[i]
l1 = [54,35,89,21,72,13]
selction_Sort(l1)
print(l1)
   