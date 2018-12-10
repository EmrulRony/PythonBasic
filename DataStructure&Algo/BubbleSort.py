item_list=[2,5,3,9,6,10,0]
len = len(item_list)

for i in range(0,len):
    for j in range (0,len-i-1):
        if (item_list[j]>item_list[j+1]):
                temp=item_list[j]
                item_list[j]=item_list[j+1]
                item_list[j+1]=temp

print(item_list)

# Time complexity O(n**2)
# Space complexity O(1)
