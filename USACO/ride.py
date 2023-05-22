"""
ID: joshua.31
PROG: ride
LANG: PYTHON3
"""

file_input = open('ride.in', 'r').read().lower().split('\n')

character_map = ' abcdefghijklmnopqrstuvwxyz'

l1 = 1
l2 = 1
for character in file_input[0]:
    l1 *= character_map.index(character)

for character in file_input[1]:
    l2 *= character_map.index(character)

out = open('ride.out', 'w')
out.write('GO\n' if l1 % 47 == l2 % 47 else 'STAY\n')
out.close()

