item_list=[2,4,6,9,12,48,50,55,70,80,82,100]
len = len(item_list)

x= int (input("Enter the number u want to search"))

left = 0
right = len-1
found=False

while (left<=right):
	mid = int ((left+right)/2)
	if (item_list[mid]==x):
		found=True
		print("The number is found at, ",item_list.index(x));
		break
	elif (x<item_list[mid]):
		right=mid-1
	elif(x>item_list[mid]):
		left=mid+1

if (found==False):
	print("The number is not avaible in the list")





