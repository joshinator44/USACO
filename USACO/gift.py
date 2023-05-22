from typing import Dict

def divideAndFind(total, divisor):
  if(divisor != 0):
    amountForEach = int(total)//int(divisor)
    remainder = int(total)%(divisor)
  else:
    amountForEach = 0
    remainder = 0
  return amountForEach, remainder
  
fhand = open('gift1.in', 'r').read().splitlines()
groupsize = int(fhand[0])
bankAcc: Dict[str, int] = {
  
}

for i in range(1, groupsize + 1):
  bankAcc.update({fhand[i]: 0})
  
#print(bankAcc)

def getGiverAndAmounts(num):
  giver = fhand[num]
  amounts = fhand[num+1].split(' ')
  total = amounts[0]
  divisor = amounts[1]
  return(giver, total, divisor)


# print(getGiverAndAmounts(7))
#print(fhand[7])

#print(len(fhand))
#print(groupsize)
giver = ""
peopleReceiveCount = 0
amountToGive = 0

for j in range((int(groupsize) + 1), len(fhand)):
  if(peopleReceiveCount == 0):
    giver = fhand[j]
    print("Giver is: " + giver)
    peopleReceiveCount = -1
  elif(peopleReceiveCount == -1):
    amountToGive, peopleReceiveCount = map(int, fhand[j].split())
    amountToGive = amountToGive // peopleReceiveCount if peopleReceiveCount != 0 else 0
    
  
