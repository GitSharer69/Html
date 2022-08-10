


# inPti=int(input("place in a number "))
# if inPti<0:
#      print("neg")
# elif inPti>0:
#      print("pos")
# else:
#     print("start again")
# if inPti%2==0:
#     print("even")
# else:
#     print("odd")
# age=int(input("enter age..."))
# if age>=18:
#     print("you can vote")
# else:
     #print("you are too small")
# inPt=input("type green or red ")
# if inPt=="green":
#     print("go")
# else:
#     print("stop")
# inPt2i=int(input("type number "))
# if inPt2i%5>=1:
#     print("isn't devisable")
# else:
#     print("is devisable")

# I1=int(input("type in your first number "))
# I2=int(input("type in your second number "))
# if I1>I2:
#     print(I1,"is larger")
# elif I1==I2:
#     print("they are the same number")
# else:
#     print(I2,"is larger")



# S=int(input("plave salery "))
# Tax=int(input("place tax for your bracket "))
# Salery=S//100
# output=Salery*Tax
# print("the taxes you need to pay is",output)
# salery=int(input("put in salery "))
# if salery>0 and salery<18000:
#     tax=0
# elif salery > 18000 and salery<37000:
#     tax=salery*(19/100)
# elif salery > 37000 and salery < 90000:
#     tax= salery*(32/100)
# elif salery> 90000:
#     tax= salery*(37/100)
# else:
#     print("invalid")
#     exit()
# print("the tax computed is",tax,"salery after tax deduction would be",salery-tax)
# vowel=['a','e','i','o','u','A','E','I','O','U']
# inChar=input("enter a letter ")
# if inChar=='a' or inChar=='e' or inChar=='i' or inChar=='o' or inChar=='u':
#     print("vowel")
# else:
#     print("not vowel")


# x,y,z=map(int,input("enter 3 angles ").split(" "))
# print(x+y+z)

# if x==y and x==z and y==x and x==z:
#      print("Equalateral")
# elif x==y and x!=z:
#      print("Isosceles")
# else:
#      print("Scalene")



# inpu=int(input("put in number"))
# to=int(input("put in number"))
# i=-1
# while (i<=to):
#      i=i+1
#      print(inpu,'x',i,'=',inpu*i)

# counters=range(0,10,3)
# print(counters[2])
# for i in range(0,10):
#      print(i)
# a = int(input('Give amount: '))
# for i in range(0,10):
#      def fib(n):
#           a, b = 0, 1
#           for _ in range(n):
#                yield a
#                a, b = b, a + b

# print(list(fib(a)))

# for i in range(5,201,5):
#      if i<20:
#           continue
#      print(i)
#      if i>99:
#           break







# for i in range(1,21):
#      print(i,"square = ",i*i)






# def greet(name):
#      print("hi",name)
# greet("name")
# def max(num1,num2):
#      if num1>num2:
#           print(num1)
#      else:
#           print(num2)
# numb1=int(input())
# numb2=int(input())
# max(numb1,numb2)

# def fac(a):
#      a*fac(a-1)
# print(fac(2))

import array as arr
a = arr.array('i', [1,2,3,4,5,6,7,8,9,10])
print ("the new array is :", end =" ")
print (a)
a.insert(3,8888)
a.append(20)
print(a)

