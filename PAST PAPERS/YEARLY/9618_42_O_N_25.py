# Q1
"""
class Bird:
    def __init__(self, DistancePerHour,Species):
        self.__Species = Species
        self.__DistancePerHour = DistancePerHour
        self.__XPosition = 500.0
        self.__YPosition = 500.0
    def GetSpecies(self):
        return self.__Species
    def GetPosition(self):
        return (f"X = {self.__XPosition} Y = {self.__YPosition}")
    def Move(self, Direction, Min):
        Distance = (self.__DistancePerHour/60)*Min
        match Direction:
            case "N":
                self.__XPosition += Distance
            case "S":
                self.__XPosition -= Distance
            case "E":
                self.__YPosition += Distance
            case "W":
                self.__YPosition -= Distance
    
def main():
    Bird1 = Bird(71.0,"Cockatiel")
    Bird2 = Bird(56.0,"Macaw")
    print(f"{Bird1.GetSpecies()} is the name of the bird and current positions are : {Bird1.GetPosition()}")
    print(f"{Bird2.GetSpecies()} is the name of the bird and current positions are : {Bird2.GetPosition()}")
    
    option = int(input("enter your option bird, select 1 for Macaw, select 2 for cockatiel"))
    while (option < 1) or (option > 2):
        print("selection out of range please re-enter")
        option = input("enter your option bird, select 1 for Macaw, select 2 for cockatiel")
    
    Direct = input("enter the direction the bird is travelling : North = N, South = S, East = E, West = W")
    Direct = Direct.upper()
    while not (Direct in ["N" , "S" , "E" , "W"]):
        print("please renenter direction")
        Direct = input("enter the direction the bird is travelling : North = N, South = S, East = E, West = W")
        Direct = Direct.upper()
    
    time = int(input("enter the time in minutes the bird takes to travel"))
    while (time < 0) or (time > 500):
        print("the minutes are out of range")
        time = int(input("enter the time in minutes the bird takes to travel"))
    
    match option:
        case 1:
            Bird1.Move(Direct, time)
            print(Bird1.GetPosition())
        case 2:
            Bird2.Move(Direct, time)
            print(Bird2.GetPosition())
            
main()
"""

#Q2
'''
import random 
Num = random.sample(range(0,101),20)
#print (Num)
 
def PrintArray(Arr):
    for i in range(len(Arr)):
        print(Arr[i] , end=" ")

def BubbleSort(arr):
    Top = len(arr) - 1
    swap = True
    while (Top>1) and (swap == True):
        swap = False
        for i in range(Top):
            if ( arr[i] > arr[i+1] ):
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
                swap = True
        Top = Top - 1
    return arr

PrintArray(Num)

Arr = BubbleSort(Num)
print("\n", end ="")
PrintArray(Arr)
      
def RecursiveBinarySearch(arr,lb,ub,find):
    
    if lb>ub:
        return -1
    mv = int((lb+ub)/2)
    
    if find < arr[mv]:
        return RecursiveBinarySearch(arr,lb,mv-1,find)
    elif find > arr[mv] :
        return RecursiveBinarySearch(arr,mv+1,ub,find)
    else:
        arr[mv] == find
        return mv
    
print("\n", end="")
print(RecursiveBinarySearch(Arr,0,19,12))
'''

#Q3



TreeArray   = [[-1, -1, -1] for _ in range(50)]
RootPointer = -1
FreeNode    = 0

# ── Part 3(b) ── AddNode() 
def AddNode(Data):
    global TreeArray
    global RootPointer
    global FreeNode

    # Check if tree is full
    if FreeNode == 50:
        print("The tree is full")
        return

    # Store data in the next free node
    TreeArray[FreeNode][1] = Data       # set data
    TreeArray[FreeNode][0] = -1         # left pointer  = null
    TreeArray[FreeNode][2] = -1         # right pointer = null
    NewNode   = FreeNode
    FreeNode += 1

    # If tree is empty, new node becomes root
    if RootPointer == -1:
        RootPointer = NewNode
        return

    # Traverse the tree to find the correct position
    CurrentNode = RootPointer
    while True:
        if Data < TreeArray[CurrentNode][1]:        # go left
            if TreeArray[CurrentNode][0] == -1:     # left is empty, insert here
                TreeArray[CurrentNode][0] = NewNode
                return
            else:
                CurrentNode = TreeArray[CurrentNode][0]
        else:                                        # go right
            if TreeArray[CurrentNode][2] == -1:     # right is empty, insert here
                TreeArray[CurrentNode][2] = NewNode
                return
            else:
                CurrentNode = TreeArray[CurrentNode][2]

# ── Part 3(d) ── WriteAllToFile()
def WriteAllToFile():
    try:
        with open("Tree.txt", "w") as f:
            for i in range(50):
                left  = TreeArray[i][0]
                data  = TreeArray[i][1]
                right = TreeArray[i][2]
                f.write(str(left) + "," + str(data) + "," + str(right) + "\n")
        print("Tree successfully written to Tree.txt")
    except Exception as e:
        print("Error writing to file:", e)



import os

file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "TreeData.txt")

with open(file_path, "r") as f:
    for line in f:
        value = line.strip()
        if value != "":
            AddNode(int(value))


WriteAllToFile()