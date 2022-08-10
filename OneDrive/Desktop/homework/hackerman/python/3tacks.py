

from math import gamma

from matplotlib import widgets


maininp=input("chose 1 2 3 or 4 to leave")
if maininp == "1":
    hobbies=["hobbies ="]
    foods=["foods ="]
    games=[]
    name=input("what is your name")
    while True:
        
        inp=input("enter 1 if u want to add hobbies enter 2 if u want to add foods enter 3 if u want to leave and check your enteries")
        if inp=="1":
            print("doing 1")
            adding=str(input("add wahat you want to add"))
            hobbies.append(adding)
        elif inp=="2":
            print("doing 2")
            adding=str(input("add wahat you want to add"))
            foods.append(adding)
        else:
            games.append(name)
            games.append(hobbies)
            games.append(foods)
            print(games)
            break
elif maininp=="2":

    for i in range(2008):
        if i%2==0:
            print(i)
        else:
            pass

elif maininp=="3":
    def moon_weight(weight,increasingwight,timeonmoon):
        for i in range(timeonmoon):
            print(weight*0.165)
            weight=weight+increasingwight
    inp=int(input("weight"))
    inp2=float(input("how much in your weight increasing"))
    inp3=int(input("how long are you staying"))
    moon_weight(inp,inp2,inp3)
else:
    print("end")










