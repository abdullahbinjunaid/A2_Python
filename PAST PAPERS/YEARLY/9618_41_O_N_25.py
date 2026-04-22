# Q1: Answer
"""
Stack = [None]*30
TopOfStack = -1

def Push(num):
    global TopOfStack
    if TopOfStack == len(Stack) - 1:
        return False
    else:
        TopOfStack += 1
        Stack[TopOfStack] = num
        return True
    
def Pop():
    global TopOfStack
    if TopOfStack == -1:
        print("Stack is empty")
        return -999
    else:
        data = Stack[TopOfStack]
        Stack[TopOfStack] = None
        TopOfStack -= 1
        print(f"The value which was popped was {data}")
        return data

def FindValues():
    data = Pop()
    max = data 
    min = data
    while data != -999:
        if data > max :
            max = data
        if data < min :
            min = data
        data = Pop()
    print(f"The largest number in the stack : {max}")
    print(f"The smallest number in the stack : {min}")



    

def main():
    import random
    Input = random.randint(0,1000)
    flag = Push(Input)
    while flag != False:
        Input = random.randint(0,1000)
        flag = Push(Input)
    print("Stack Full")
    print(Stack)
    FindValues()

main()
"""

# Q2:
"""
class Train:
    def __init__(self, TrainIdNumber, Route):
        self.__TrainIdNumber = TrainIdNumber
        self.__Route = Route
    def GetTrainIdNumber(self):
        return self.__TrainIdNumber
    def GetRoute(self):
        return self.__Route
    
Train1 = Train("12ADV", 134)
Train2 = Train("33ART", 20)
Train3 = Train("9FKF", 3)
Train4 = Train("21VBC", 24) 

class Station():
    def __init__(self, StationID, NumberPlatforms):
        self.__StationID = StationID
        self.__NumberPlatforms = NumberPlatforms
        self.__Trains = [None]*9
        self.__NumberTrains = 0
    def AddTrain(self,InputTrain):
        if self.__NumberPlatforms == self.__NumberTrains:
            print("station is full")
            return False
        else:
            i = 0
            while (self.__Trains[i] != None) and (i < 9):
                i += 1
            self.__Trains[i] = InputTrain
            self.__NumberTrains += 1 
            return True
    def GetTrains(self):
        if self.__NumberTrains == 0:
            return "There are no trains"
        else:
            print(f"The trains at station {self.__StationID}:")
            for i in range(self.__NumberTrains + 1):
                
                print(f"{self.__Trains[i].GetTrainIdNumber()} on route number {self.__Trains[i].GetRoute()}")





station1 = Station("STH", 2)
station2 = Station("NTH", 1)

flag = station1.AddTrain(Train1)
if flag == False:
    print("Station is full")
flag = station1.AddTrain(Train2)
if flag == False:
    print("Station is full")
flag = station1.AddTrain(Train3)
if flag == False:
    print("Station is full")
flag = station2.AddTrain(Train4)
if flag == False:
    print("Station is full")

"""


# Q3:
class Record:
    def __init__(self,Key,String):
        self.Key = Key
        self.String = String

HashTable = []


def InitialiseHashTable():
    global HashTable
    HashTable = [[Record(-1,"")]*10 for i in range(100)]

def Hash(key):
    return key % 100

def InsertData(Obj):
    global HashTable
    value = Hash(Obj.Key)
    i = 0
    while HashTable[value][i] == None:
        i += 1
    HashTable[value][i] = Obj

def ReadData():
    import os
    file_path = os.path.dirname(__file__)
    file = os.path.join(file_path , "HashTableData.txt")
    with open(file,"r") as f:
        for Data in f:
            Data = Data.strip()    
            print(Data)
            i = 0
            while Data[i] != ",":
                i += 1
                print(i)
            key = Data[0:i]
            string = Data[i+1:]
            Object = Record(int(key),string)
            InsertData(Object)

def GetRecord(Find):
    pass





        