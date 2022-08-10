def moon_weight(weight,increasingwight,timeonmoon):
        for i in range(timeonmoon):
            print(weight*0.165)
            weight=weight+increasingwight
inp=int(input("weight"))
inp2=float(input("how much in your weight increasing"))
inp3=int(input("how long are you staying"))
moon_weight(inp,inp2,inp3)