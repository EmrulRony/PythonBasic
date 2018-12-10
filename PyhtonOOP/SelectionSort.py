item_list=[2,5,3,9,6,10,0]
len = len(item_list)
for x in range (0,len):
    min = x
    for y in range (x+1,len):
        if (item_list[min]>item_list[y]):
            min=y

    if (min!=x):
        temp=item_list[x]
        item_list[x]=item_list[min]
        item_list[min]=temp

print(item_list)

# Time complexity O(n**2)
# Space complexity O(1)
