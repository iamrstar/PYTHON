def quick_sort(data_list):
    if len(data_list)<=1:
        return data_list
    else:
        pivot = data_list[0]
        less = [i for i in data_list[1:] if i <= pivot]
        greater = [i for i in data_list[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)
my_list = [54,26,93,17,77,31,44,55,20]
print(quick_sort(my_list))
