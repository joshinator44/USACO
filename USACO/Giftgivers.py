"""
ID: Joshua.31
LANG: Python3
PROG: gift1
"""
# This will open the file and allow to read and write
# fin = open("gift1.txt", 'r').read().splitlines()
# fout = open("gift1.in", 'w')
fin = "5|dave|laura|owen|vick|amr|dave|200 3|laura|owen|vick|owen|500 1|dave|amr|150 2|vick|owen|laura|0 2|amr|vick|vick|0 0"
fin = fin.split("|")
print(fin)
# Grab number of people in a integer value
people_counter = False
numPeople = int(fin[0])
print(numPeople)
namsPeople = fin[1:numPeople+1]
print(namsPeople)
ppl_money = {fin[1]: "0", fin[2]: "0", fin[3]: "0", fin[4]: "0", fin[5]: "0"}


# This gives the names of all the people


    

