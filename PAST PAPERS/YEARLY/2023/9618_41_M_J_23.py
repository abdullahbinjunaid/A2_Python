#Q1
'''
import os

def PrintArray(array):
    for i in array:
        print(str(i), end=" ")

def LinearSearch(array , find):
    amount = 0
    for i in range (len(array)):
        if array[i] == find:
            print(f"{find} was found at index {i}")
            amount += 1
    return amount


#----MAIN PROGRAM----
def main():
    global DataArray
    DataArray = []
    
    file_path = os.path.dirname(__file__)
    file = os.path.join(file_path,"Data.txt")
    if os.path.exists(file):
        with open(file , "r") as f:
            for i in f:
                Line = int(i.strip())
                DataArray.append(Line)
    else:
        print("The file doesn't exists") 

    PrintArray(DataArray)
    print('\n',end="")
    try:
        Tofind = int(input("enter a integer b/w 0 and 100 to search in the array"))
        while (Tofind < 0) or (Tofind > 100):
            print("The input is out of range please re-enter")
            Tofind = int(input("enter a integer b/w 0 and 100 to search in the array"))
        count = LinearSearch(DataArray,Tofind)
        print(f"The number {Tofind} was found {count} times")
    except ValueError:
        print("incorrect data type entered")
    else:
        print("!")
    finally:
        print("program completed")


main()
'''
#Q2
'''
class Vehicle:
    def __init__(self,ID,MaxSpeed,IncreaseAmount):
        self.__ID = ID #String
        self.__MaxSpeed = MaxSpeed #Integer
        self.__CurrentSpeed = 0 #Integer
        self.__IncreaseAmount = IncreaseAmount #Integer
        self.__HorizontalPosition = 0 #Integer
    def GetCurrentSpeed(self):
        return self.__CurrentSpeed
    
    def GetIncreaseAmount(self):
        return self.__IncreaseAmount
    
    def GetHorizontalPosition(self):
        return self.__HorizontalPosition
    
    def GetMaxSpeed(self):
        return self.__MaxSpeed
    
    def SetCurrentSpeed(self,Speed):
        self.__CurrentSpeed = Speed
    
    def SetHorizontalPosition(self,Position):
        self.__HorizontalPosition = Position
    
    def IncreaseSpeed(self):
        self.__CurrentSpeed += self.__IncreaseAmount
        if self.__CurrentSpeed > self.__MaxSpeed:
            self.__CurrentSpeed = self.__MaxSpeed
        self.__HorizontalPosition += self.__CurrentSpeed

class Helicopter(Vehicle):
    def __init__(self, ID, MaxSpeed, IncreaseAmount,VerticalChange,MaxHeight):
        super().__init__(ID, MaxSpeed, IncreaseAmount)
        self.__VerticalPosition = 0 #Integer
        self.__VerticalChange = VerticalChange #Integer
        self.__MaxHeight = MaxHeight #Integer
    
    def GetVerticalPosition(self):
        return self.__VerticalPosition
    
    def IncreaseSpeed(self):
        
        self.__VerticalPosition += self.__VerticalChange
        if self.__VerticalPosition > self.__MaxHeight:
            self.__VerticalPosition = self.__MaxHeight
        # speed and horizontal update using parent getters/setters
        newSpeed = self.GetCurrentSpeed() + self.GetIncreaseAmount()  
        if newSpeed > self.GetMaxSpeed():
            newSpeed = self.GetMaxSpeed()
        self.SetCurrentSpeed(newSpeed)                                 
        self.SetHorizontalPosition(self.GetHorizontalPosition() + newSpeed)


#The question only said procedure, hence a method and a separate procedure can work
#Either we have made separate methods in each class for outputing, or done this both are good
def Output(vehicle):
    # Output horizontal position and speed [cite: 161]
    horiz = vehicle.GetHorizontalPosition()
    speed = vehicle.GetCurrentSpeed()
    print(f"Horizontal Position: {horiz}")
    print(f"Current Speed: {speed}")
    
    # If vehicle is a helicopter, output vertical position [cite: 162]
    if isinstance(vehicle, Helicopter):
        print(f"Vertical Position: {vehicle.GetVerticalPosition()}")

def main():
    Vehicle1 = Vehicle("Tiger",100,20)
    Vehicle2 = Helicopter("Lion",350,40,3,100)
    Vehicle1.IncreaseSpeed()
    Vehicle1.IncreaseSpeed()
    Vehicle2.IncreaseSpeed()
    Vehicle2.IncreaseSpeed()
    Output(Vehicle1)
    Output(Vehicle2)

main()
'''        
#Q3
Animal = [None]*20
Colour = [None]*10
AnimalTopPointer = 0
ColourTopPointer = 0

def PushAnimal(Data):
    global Animal
    global AnimalTopPointer
    if AnimalTopPointer == 20:
        print("The Stack is full")
        return False
    else:
        Animal[AnimalTopPointer] = Data
        AnimalTopPointer = AnimalTopPointer + 1
        return True
    
def PopAnimal():
    global Animal
    global AnimalTopPointer
    ReturnData = ""
    if AnimalTopPointer == 0:
        print("The stack is empty")
        return ""
    else:
        ReturnData = Animal[AnimalTopPointer]
        AnimalTopPointer = AnimalTopPointer - 1
        return True


def PushColour(Data):
    global Colour
    global ColourTopPointer
    if ColourTopPointer == 20:
        print("The Stack is full")
        return False
    else:
        Colour[ColourTopPointer] = Data
        ColourTopPointer = ColourTopPointer + 1
        return True
    
def PopColour():
    global Colour
    global ColourTopPointer
    ReturnData = ""
    if ColourTopPointer == 0:
        print("The stack is empty")
        return ""
    else:
        ReturnData = Animal[ColourTopPointer]
        ColourTopPointer = ColourTopPointer - 1
        return True



import os    
def ReadData():

    file_Path = os.path.dirname(__file__)
    file = os.path.join(file_Path,"AnimalData.txt")
    if os.path.exists(file):
        with open(file,"r") as f:
            for i in f:
                Data = i.strip()
                print(PushAnimal(Data))
    else:
        print("The file doesn't exists")
    
    file2 = os.path.join(file_Path,"ColourData.txt")
    if os.path.exists(file2):
        with open(file2,"r") as f:
            for i in f:
                Data = i.strip()
                print(PushColour(Data))
    else:
        print("The file doesn't exists")

def OutputItem():
    ItemAnimal = PopAnimal()
    ItemColour = PopColour()
    if ItemColour == "":
        print(PushAnimal(ItemAnimal))
        print("No colour")
    if ItemAnimal == "":
        print(PushColour(ItemColour))
        print("No animal")
    
ReadData()
OutputItem()
OutputItem()
OutputItem()
OutputItem()