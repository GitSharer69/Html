"""
Your program should read from the file oilin.txt. The first line of this file will contain three
space-separated integers R, C and K. The following R lines will each contain C characters, each
of which will be '#' or '.' representing land and sea squares respectively. Exactly one character in
the entire grid will be '$', representing the oil rig at sea
"""



oilin = open('oilin.txt')

row_count, column_count, days = [int(line.strip()) for line in oilin.readline().split()]

rows = []

for i in range(row_count):
    rows.append(oilin.readline())



oilin.close()
