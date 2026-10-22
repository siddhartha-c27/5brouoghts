
age = int(input("enter age"))
if(age<18) :
    print("your minor")
else:
    print("majour")


#elif
n =int(input("enter number")) 
if(n<0) :
    print("number is negative")
elif(n==0) :
    print("number is both + and -")
else :
    print("number is positive")

# #nested if
# # b = int(input("enter age for blood donation :"))
# # if(b>=18 and b<=65) :
# #     print("age is ok next will go for weight check up ")
# #     weight = int(input("enter weight"))
# # elif(weight >= 50) :
# #     print("ok next blood level")
# #     level = int(input("enter blood level"))
# #     if(level >=12.5) :
# #         print("person can donate blood")
# #     else:
# #         print("ineligibe:blood level not support")
# # else:
# #     print("ineligible :weightn not support")
# #     else :
# #         print("age dont")
# #loops 
# #for loop 
# name = "spongebob"
# # for  i in name :
# #     print(i)
# #     print(i,end=",")
# #     #list
# # colors =['red','blue','yellow']
# # for i in colors :
# #     print(i)
    #range
# for k in range(34) :
#         print(k)
# for i in range(1,8):
#     print(i)
# for j in range(1,100,20) :
#     print(j)
    
    
    #while loop
    #increment
i=0;
while(i<=4) :
    print(i)
    i=i+1
    #decrement
count =9
while(count>=0) :
    print(count)
    count =count-1
#else in while loop
i = 8
while(i>=0) :
    print(i)
    i=i-1
else:
    print("whatever")
