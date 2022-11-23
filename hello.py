# print("helloworld")
# #print("welcome")

# name=input("Enter your name: ")
# print("welcome ",name)


#adding two numbers
#firstnum=int(input("Enter firstnumber:"))
#secondnum=int(input("Enter secondnumber:"))
#adding=firstnum+secondnum
#print("Totalvalues", adding)

#Using module
#import datetime
#current_date=datetime.datetime.now()
#print("the currentdateandtime is:",current_date)

#Finding str len
#lengthofstring=str(input("Enter the value: "))
#calvalue=len(lengthofstring)
#print("Length of string:",calvalue)

# defining a strfunction
#def str_function(paramters):
 #   return len(paramters)

#inputofstring=str(input("Enter the value: "))
#print("len=",str_function(inputofstring))


#just creating def to print without parameter
# def helloworld():
#     print("helloworldfrom the function")
    
# helloworld()

#just creating def to print with parameter
#  def helloworld(inputvariable):
#      print("helloworld from the function",inputvariable)

# inputofstring=str(input("Enter the value: "))
# helloworld(inputofstring)

def add(first_no,second_no):
   sum=(first_no+second_no)
   print(sum)

def sub(first_no,second_no):
    sub=(first_no-second_no)
    print(sub)

def mul(first_no,second_no):
    mul=(first_no*second_no)
    print(mul)

def div(first_no,second_no):
   div=(first_no%second_no)
   print(div)

num1= int(input("Enter the value for first no:  "))
num2= int(input("Enter the value for second no:  "))
print("Enter which operation would you like to perform?")
option = str(input("Enter any operation=sum,sub,mul,div: ")).lower()
print(option)
if option=="sum":
    add(num1,num2)
elif option=="sub":
    sub(num1,num2)
elif option=="mul":
    mul(num1,num2)
elif option=="div":
    div(num1,num2)
else:
    print("Please enter the following options=sum,sub,mul,div: ")
