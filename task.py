#Find the largest item from a given list 
# num = [3,5,7,8,1,2,55,33,22,66,33,100,109]
# num.sort()
# print("Largest element is:", max(num))

# num = [3,5,7,8,1,2,55,33,22,66,33,100,109]
# maxnum=(max,num)
# print(maxnum)

# Creating def for maxvalue

# def largestval(large):
#     print(max(large))
    
# num = [3,5,7,8,1,2,55,33,22,66,33,100,109]
# largestval(num)

#finding smallest function
# def lesserval(small):
#     print(min(small))
    
# num = [3,5,7,8,1,2,55,33,22,66,33,100,109]
# lesserval(num)

#Generate a Python list of all the even numbers between 4 to 30
# start = int(input("Enter the start of range: "))
# end = int(input("Enter the end of range: "))
# c=[]
# # iterating each number in list
# for num in range(start, end):
# # checking condition
#    if num % 2== 0: 
#        c.append(num)
# print(c)

#starting program to find even num
# startnum=int(4);endnum=int(30);
# c=[]
# for num in range(startnum, endnum):
# # checking condition
#    if num % 2== 0: 
#        c.append(num)
# print(c)

#basic program of append
# start=(4)
# end= (int(input("Enter the end of range:",)))
# # print(end)
# # start.append(end)
# newstart=tuple(start)+(end,)
# print(newstart)
# nums=range(start)
# print(nums)
# for num in nums:
    
#     if num % 2==0:
#       print(type(num))

# start=(4,)
# print("Start",type(start))
# end= (input("Enter the end of range:",))
# # print("end",type(end))
# newstart = start +(int(end),)
# # print(newstart)
# for num in range(newstart):
#     if num % 2==0:
#         print(type(num))

start=(4)
end= (input("Enter the end of range:",))
for num in range(int(start), int(end)):
    if num % 2==0:
        print((num))
