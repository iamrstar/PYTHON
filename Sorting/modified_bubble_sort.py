def modified_bubble_sort(data_List):
    flag = False
    for r in range(1,len(data_List)):
        flag = False
        for i in range (len(data_List)-r):
            if data_List[i]>data_List[i+1]:
                data_List[i],data_List[i+1]=data_List[i+1],data_List[i]
                flag = True
        if not flag:
            break
bubble = [34,67,12,89,25,50]
modified_bubble_sort(bubble)
print(bubble)

                
