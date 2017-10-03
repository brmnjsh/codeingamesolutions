#temperatures
#https://www.codingame.com/ide/puzzle/temperatures

import sys,math

n = int(input())
temps = input()  

temperatures = temps.split()
temperatures = list(map(int, temperatures))
answer = 0

for temp in temperatures:
    if answer == 0:
        answer = temp
    elif (abs(temp) < abs(answer)) or (abs(temp) == abs(answer) and temp > 0):
        answer = temp     

print(temps, file=sys.stderr)
print(answer)