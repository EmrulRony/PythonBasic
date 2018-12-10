# for x in range (1,5):
#     for y in range (1,5):
#          print(x,end="");
#     print();
# output:

# 1111
# 2222
# 3333
# 4444

# for x in range(1,5):          #
#     for y in range(1,x+1):
#         print(y,end="");
#     print();
# output:

# 1
# 12
# 123
# 1234

# for num in range(6):
#     for i in range(num):
#         print (num, end="")
#     print()
#
# output
#
# 1
# 22
# 333
# 4444
# 55555


# for i in range (1,6):
#     for x in range(1,7-i):
#         print ("*", end ="");
#     print();

#output:
# *****
# ****
# ***
# **
# *


# for i in range (1,6):
#     for x in range (1,i+1):
#         print ("*", end ="");
#     print();

#output:
# *
# **
# ***
# ****
# *****

# for i in range(1,6):
#     for x in range (i,0,-1):
#         print(x,end="");
#     print();
#
# output
# 1
# 21
# 321
# 4321
# 54321

#print("Fifth Number Pattern")
#
# for i in range (1,6):
#     for j in range(0,i,1):
#         print(2**j, end="");
#     for k in range (-1+j,-1,-1):
#         print(2**k,end="")
#     print();
#
# 1
# 121
# 12421
# 1248421
# 1248168421