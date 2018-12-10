list_of_element=[2,100,5000,523,33,444,523,5532,234,1,3,5,8,14,18]

print(len(list_of_element))
x=int(input("Enter the num you want to search "))

found=False

for i in range (0,len(list_of_element)):
    if (list_of_element[i]==x):
        found=True
        print("Num found ",x, " in index of ", i)
        break

if (found==False):
    print("The num is not in the array :(")

