'''
def kingofPops():
    nPop=input("How many popS?")
    nPop=int(nPop)
    pricePop=12.5
    tipAmt = input("Hwo much tip")
    tipAmt = float(tipAmt)
    total=pricePop*nPop*(1+tipAmt)
    print("Your total is $" + str(total))

kingofPops()

def comboOrder():
    entree=input("Enter entree? ")
    drink=input("Enter drink ")
    side=input("Enter side? ")
    print("Your order is" + entree + "," + drink + "," + side)

comboOrder()





import calendar

operation = [calendar.THURSDAY]

print(operation)
'''
import numpy as np

a = np.matrix([[4, 2.1],
               [4.2, 2.2]]) #2145

print(np.linalg.norm(a)*np.linalg.norm(np.linalg.inv(a)))
print(np.linalg.cond(a, p='fro'))