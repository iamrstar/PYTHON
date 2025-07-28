def bubble_sort(data_List):
    for r in range(1,len(data_List)):
        for i in range (len(data_List)-r):
            if data_List[i]>data_List[i+1]:
                data_List[i],data_List[i+1]=data_List[i+1],data_List[i]
bubble = [5,4,3,2,1]
bubble_sort(bubble)
print(bubble)

               
