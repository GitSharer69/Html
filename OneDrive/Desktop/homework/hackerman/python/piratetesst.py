# X = input()
# L = input()
# Y = input()
# print(X,Y,L)
# with open('piratein.txt') as f:

"""
     5
<-------> (boat)  x

      10 (island)
<---------------> l
   3
<-----> (dest)    y

"""

piratein = open('./piratein.txt')
l, x, y = [int(line.strip()) for line in piratein.readlines()]
piratein.close()
left = x + y
right = (l - x) + (l - y)
print(min(left, right))