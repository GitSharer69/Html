





# tuple1=(1,2,3,4,5)
# # tuple2=tuple(1,2,3,4,5)
# print(tuple1[0:2])
# fruits=("apple","mango","papaya","pineapple","cherry")
# (yellow,*green,red)=fruits
# print(yellow)
# print(green)
# print(red)
# nums=(1,2,3,2,1,8,5,6,3,35,6,54,6,5,4,654,64,6)
# list1=[set(nums)]
# print(list1)
# DaysA = set(["Mon","tue","wed"])
# DaysB = set (["wed","thu","fri","sat","sun"])
# Alldays = DaysA & DaysB
# print(Alldays)
# books=["harry potter 1 index = 0","harrypotter 2 index = 1","harrypotter 3 index = 2","harrypotter 4 index = 3"]
# cart1 = ["cart = "]
# while True:
#     inp = input("press 1 for avalable books\npress 2 to get book\npress 3 to check cart\n press 4 to end\n")
#     if inp=='1':
#         print(books)
#         pass
#     elif inp=='2':
#         removing_book=int(input())
#         cart1.append(books[removing_book])
#         # books.pop(removing_book)
#         pass
#     elif inp=='3':
#         print(cart1)
#         pass

#     else:
#         break
# dictionary





# a = "name"
# personinfo = {a:'Shravesh','gender':'male','age':'14','postcode':'3051'}
# # personinfo['name']
# # print("name",personinfo[a])
# # print("gender",personinfo['gender'])
# # print("age",personinfo['age'])
# # print(personinfo.keys())
# # personinfo['favor']=personinfo
# # print(personinfo)


# # personinfo.get('name')

# for x in personinfo.keys:
#     print(x,personinfo.get(x))

# def printing(a,b):
#     print('first',a)
#     print('last',b)



# Balence=0
# while True:
#     maininput=input("type 1 to add account\ntype 2 to deposit money\ntype 3 to withdraw money\n type 4 to show balence\n type 5 to exit system\n")
#     if maininput=="1":
#         nameinput=input("type in you name\n")
#         Gender=input("enter gender")
#         Age=input("enter age")
#         code=int(input("make account code"))
#         bankname=input("enter bank name")
#         ATM={nameinput:{'gender':Gender,'age':Age,'securitycode':code,'bankname':bankname,'Balence':Balence}}
#         print(nameinput,"\n")
#     elif maininput=="2":
#         depositamount=int(input("put in amount you want to put in\n"))
#         try:
#             ATM[nameinput]['Balence']=ATM[nameinput]['Balence']+depositamount
#         except:
#             print("error")
#     elif maininput=="3":
#         withdrawamount=int(input("put in amount you want to withdraw\n"))
#         try:
#             if ATM[nameinput]['Balence']>withdrawamount:
#                 try:
#                     ATM[nameinput]['Balence']=ATM[nameinput]['Balence']-withdrawamount
#                 except:
#                     print("error")
#             else:
#                 print("insufficent funds\n")
#         except:
#             print("profile non existant\n")

#     elif maininput=="4":
#         print(ATM[nameinput]['Balence'])

#     else:
#         print(ATM,"\nlogging out")
#         break





"""""""""
products = {"cherry":10,"pineapple":20,"grape":15,"avacado":30}
cart = {"total":0,'cartproducts':[]}
while True:
    maininput=input("type 1 to add to cart\ntype 2 to remove from cart\ntype 3 to view cart\n type 4 to cost\n type 5 to checkout\n")
    if maininput == "1":
        print("option 1 chosen")
        print(products)
        
        chosenone=input("chose an item")
        
        cart[chosenone]=products[chosenone]
        cart["total"] = cart["total"]+cart[chosenone]
        

    elif maininput == "2":
        print("option 2 chosen")

    elif maininput == "3":
        print("option 3 chosen")
        print(cart)

    elif maininput == "4":
        print("option 4 chosen")
        print(cart["total"])


    else:
        print("option 5 chosen")
        break
"""""""""




# def print_inventory(dct):
#     print("Items held:")
#     for item, amount in dct.items():  # dct.iteritems() in Python 2
#         print("{} ({})".format(item, amount))
# import sys
# import time
# studentlist={}
# def slowprint(s):
# 	for c in s + '\n':
# 		sys.stdout.write(c)
# 		sys.stdout.flush()
# 		time.sleep(1./10)


# while True:
#     ip = input("start")
#     if ip == "1":
#         name=str(input(slowprint("Name")))
#         gender=str(input(slowprint("Gender")))
#         classs1=str(input(slowprint("Class")))
#         marks=int(input(slowprint("Marks")))
#         studentlist.update({name:{'gender':gender,classs1:marks}})
#         print_inventory(studentlist[name])
#     elif ip == "2":
#         name2=str(input(slowprint("student name")))
#         classs2 = str(input(slowprint("class to update")))
#         newmark = int(input(slowprint("new marks")))
#         newset={classs2:newmark}
#         studentlist[name2].update(newset)
#         print_inventory(studentlist[name])
#     elif ip == "3":
#         print_inventory(studentlist)
#         print_inventory(studentlist[name])
#     else:
#         slowprint("exiting")
#         print_inventory(studentlist)
#         print_inventory(studentlist[name])
#         try:
#             print_inventory(studentlist[name2])
#         except:
#             pass
#         break





def winningplayer(u):
    if u =="1":
        print("player 1 win's")
    else:
        print("player 2 win's")
def split(x):
    for i in range(0,x):
        print("####\n####")
def game(player1choicedef,player2choicedef):
    if player1choicedef == player2choicedef:
        print("tie")
    elif player1choicedef == "rock" and player2choicedef == "scissor":
        winningplayer(1)
    elif player2choicedef == "rock" and player1choicedef == "scissor":
        winningplayer(2)
    elif player1choicedef == "paper" and player2choicedef == "scissor":
        winningplayer(2)
    elif player2choicedef == "paper" and player1choicedef == "scissor":
        winningplayer(1)
    elif player1choicedef == "paper" and player2choicedef == "rock":
        winningplayer(1)
    elif player2choicedef == "paper" and player1choicedef == "rock":
        winningplayer(2)
while True:
    player1choice=input("player 1's choice")
    player2choice=input("player 2 choice")
    game(player1choice,player2choice)
    Choice=input("do you want to leave or not (yes or no)")
    if Choice == "yes":
        break
    else:
        pass



    







