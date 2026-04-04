#Encapsulation :
# 1.Bundling & 2.Access Restriction 
class Account:
    def __init__(self,balance):
        self.__balance = balance
    def deposit(self,amount):
        self.__balance += amount
        
    def get_balance(self):
        return self.__balance
    
acc = Account(1000)
print(acc.get_balance())
#print(acc.__balance)
acc.deposit(1000000)
print(acc.get_balance())
