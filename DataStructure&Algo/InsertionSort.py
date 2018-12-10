list = [9,7,8,6,5,4,3]  #799

len = len(list)

for i in range (1,len):
    key = list[i]
    left= i-1

    while (left>=0 and key<list[left]):
        list[left+1]=list[left]
        left=left-1

    list[left+1]=key

print(list)


