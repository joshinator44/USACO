
fin = open('bessie.in', 'r').read().splitlines()
print(fin)
cows = []
greater = []
lesser = []
#G is 0, L is 1
for i in range(len(fin)):
  if fin[i].split(" ")[0] == "G":
    print("G")
    cows.append(0)
    greater.append(fin[i].split(" ")[1])
  elif fin[i].split(" ")[0] == "L":
    print("L")
    cows.append(1)
    lesser.append(fin[i].split(" ")[1])
  else:
    continue


