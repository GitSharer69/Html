# name="Shravesh"
#hobby="Guitar"
#favBook="A Monster Calls"
#fullname=name+" Bestha Ramesh Kavitha"
#print("Name=",fullname)
#print("Hobby=",hobby)
#print("favourite book is = ",favBook)




#name="shravesh"
#surname="Bestha"
#age="13"
# gender="male"
# favColour="blue"
# streetName="Collins street"
# pincode="3051"
# state="victoria"
# country="Australia"
# print("My name is "+name,surname+". I am "+age,"years old. I live at",streetName,state,country,pincode)
# num1=4
# num2=7
# print(num1-num2)
# print(num1+num2)
# print(num1*num2)
# print(num1/num2)
# print(num1%num2)


# name="Joe "

# lastname="mama"
# age=13
# print(f" My full name is {name}{lastname} and my age is {age}")
# print( "my first name is %s my last name is %s i am %d" %(name,lastname,age))








#firstname="Sherlock"
#lastname="holmes"
#age="18"
#print("My age is {age} and my last name is {ln} and my first name is {fn}".format(fn=firstname,ln=lastname,age=age))
# concat (+)
# Fstring (f" My full name is {name}{lastname} and my age is {age}")
# aruement speifier ("%s,%d"%(a,b))
# format() 1)PlaceHolders 2)arguement PlaceHolders  "",format()




# # toFind="he"
# # string1="There was only half a worm in the apple. At first, Judy didn't quite comprehend what this meant. Why would only half a worm be living in an apple? she wondered. And then it dawned on her. Judy quickly spit out the bite she had just taken expecting to see the other half of the worm. It ended up being much worse than that"
# # print(string1.index(toFind))
# # print("length",len(toFind))
# # start_index=string1.find(toFind)
# # anding_index=string1.find(toFind)+len(toFind)
# # print("ending index", anding_index)
# # print(string1[start_index:anding_index])
# # toFind="Apple"
# # string1="welcome to the class. hi asdahsgdjagsdjadasd Ajay likes Apple "
# # print("STARTING INDEX",string1.find(toFind))
# # print("LENGTH",len(toFind))
# # starting_index=string1.find(toFind)
# # ending_index=string1.find(toFind)+len(toFind)
# # print("ENDING INDEX",ending_index)
# # print(string1[starting_index:ending_index+1])
# #name=input()
# #print(name)



# # Floatnumber=3232.54343
# # print(int(Floatnumber))




# #print(type(False))














toFind=input("type word to find ")
string1="There was only half a worm in the apple. At first, Judy didn't quite comprehend what this meant. Why would only half a worm be living in an apple? she wondered. And then it dawned on her. Judy quickly spit out the bite she had just taken expecting to see the other half of the worm. It ended up being much worse than that"
print("STARTING INDEX", string1.find(toFind))
print("LENGTH",len(toFind))
starting_index=string1.find(toFind)
ending_index=string1.find(toFind)+len(toFind)
print("ENDING INDEX",ending_index)
print(string1[starting_index:ending_index+1])
x= string1.count(toFind)
y= string1.endswith(toFind)
z= string1.isalpha()
print("starting location {si} ending location {ei} word found= {tf} and the length is {len} amount of {tf} = {x} does it end with {tf}? answer= {y} all alphabets={z}".format(si=starting_index,ei=ending_index,tf=toFind,len=len(toFind),x=x,y=y,z=z))


# fruit1=fruit2=fruit3="pineapple"
# print(fruit1)







#print(2%6)
# points=input()
# if points<50:
#     print("fail")
# else:
#     print("pass")
# print("do it again")
