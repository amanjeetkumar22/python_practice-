"""" 
* 
* *
* * *
* * * *
* * * * * """       
n=int(input("Enter the number:"))

# for i in range(1,n+1):
#     for j in range (1,i+1):
#         print("*",end=" ")
#     print()
"""
1
22
333
4444
55555"""
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(i,end="")
#     print()

#      * 
#     * * 
#    * * * 
#   * * * * 
#  * * * * * 

# print ("---Pyramid---")
# for i in range (1,n+1):
#     print(" "*(n-i),end=" ")
#     print("* "*i)

# # * * * * * * *
# #   * * * * * *
# #    * * * * *
# #     * * * *
# #      * * *
# #       * *
# #        *
# print ("---Reverse pyramid---")

# for j in range(n,0,-1):
#     print(" "*(n-j),end=" ")
#     print("* "*j)

# print ("---Diamond---")

# for i in range (1,n+1):
#     print(" "*(n-i),end=" ")
#     print("* "*i)

# for j in range(n-1,0,-1):
#     print(" "*(n-j),end=" ")
#     print("* "*j)

for i in range (1,n+1):
    print(" "*(i*2),end=" ")
    print("* "*i)
