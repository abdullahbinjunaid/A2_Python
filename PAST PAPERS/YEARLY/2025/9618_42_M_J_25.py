#Q1
'''
Stack = ["-1"]*20
TopOfStack = -1

def Push(Data):
    global TopOfStack
    if TopOfStack == 19:
        return -1 #Stack is full 
    else:
        TopOfStack += 1
        Stack[TopOfStack] = Data
        return 1
    
def Pop():
    global TopOfStack
    if TopOfStack == -1:
        return "-1"
    else:
        Value = Stack[TopOfStack]
        TopOfStack -= 1
        return Value


import os    
def ReadData(filename):
    file_path = os.path.dirname(__file__)
    file = os.path.join(file_path, filename)
    
    if os.path.exists(file):
        with open(file,"r") as f:
            for i in f:    
                Line = i.strip()
                flag = Push(Line)
                if flag == -1:
                    print("The stack is now full")
    else:
        print("The file doesn't exists") 




print(Stack)      

def Calculate():
    global TopOfStack
    Value1 = Pop()
    Total = int(Value1)
    
    for i in range(1,TopOfStack + 1):
        Operator = Pop()
        Value2 = Pop()
        match Operator:
            case "+":
                Total = Total + int(Value2)
            case "-":
                Total = Total - int(Value2)
            case "/":
                Total = Total / int(Value2)
            case "*":
                Total = Total * int(Value2)
            case "^":
                Total = Total ** int(Value2)
    return Total

def main():
    filename = input("enter a filename")
    ReadData(filename)
    print(Calculate())


main()

'''
'''
#Q2
class NewRecord:
    def __init__(self, Key , Item1,Item2):
        self.Key = Key 
        self.Item1 = Item1
        self.Item2 = Item2
HashTable = []
Spare = []

def Initialize():
    global HashTable
    global Spare 
    
    for i in range(200):
        HashTable.append(-1)
    for i in range(100):
        Spare.append(-1)

def CalculateHash(KeyField):
    return KeyField % 200

def InsertIntoHash(Record):
    Key = CalculateHash(Record.Key)
    if HashTable[Key] == -1:
        HashTable[Key] = Record
    else:
        #Collision Case
        i = 0
        while Spare[i] != -1:
            i += 1
        Spare[i] = Record



import os
def CreateHashTable():
    file_path = os.path.dirname(__file__)
    file = os.path.join(file_path, "HashData.txt")
    if os.path.exists(file):
        with open (file,"r") as f:
            for i in f:
                i = i.strip()
                #finding commas via find() and rfind()
                comma1 = i.find(",") #first occurence
                comma2 = i.rfind(",")#Last occurence
                key_obj = i[:comma1]
                item1_obj = i[comma1+1:comma2]
                item2_obj = i[comma2+1:]
                #print(key_obj, item1_obj, item2_obj)
                record = NewRecord(int(key_obj), int(item1_obj), int(item2_obj))
                InsertIntoHash(record)
                record = None

def PrintSpare():
    for i in Spare:
        if i != -1:
            print(i.Key)


def main():
    Initialize()
    CreateHashTable()
    PrintSpare()
main()
'''


