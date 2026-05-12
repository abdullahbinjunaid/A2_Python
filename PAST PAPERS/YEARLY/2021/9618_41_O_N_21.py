#Q1
'''
def Unknown(x,y):
    if x < y:
        print(x + y)
        return Unknown(x+1,y) * 2
    else:
        if x == y:
            return 1
        else:
            print(x + y)
            return Unknown(x-1,y) // 2


def IterativeUnknown(x,y):
    if x < y:
        counter = 1
        while x < y:
            total = x + y
            print(total)
            x = x + 1
            counter = counter * 2    
        return counter  
    else:
        if x == y:
            return 1
        else:
            counter = 1  
            while x > y:
                total = x + y 
                print(x + y)
                x = x - 1
                counter = counter // 2

            return counter
            

#----MAIN PROGRAM----
def main():
    print("The parameter values are 10, 15")
    print(Unknown(10, 15))
    print("The parameter values are 10, 10")
    print(Unknown(10, 10))
    print("The parameter values are 15, 10")
    print(Unknown(15, 10))

    print("\nIterative:")
    print("Parameters 10, 15:")
    print(IterativeUnknown(10, 15))
    print("Parameters 10, 10:")
    print(IterativeUnknown(10, 10))
    print("Parameters 15, 10:")
    print(IterativeUnknown(15, 10))
main()
'''
#Q2
'''
class Picture:
    def __init__(self,description,width,height,framcolor):
        self.__description = description #declare description string
        self.__width = width #declare width integer
        self.__height = height #declare height integer
        self.__framecolor = framcolor #declare color string
    def GetDescription(self):
        return self.__description
    def GetWidth(self):
        return self.__width
    def GetHeight(self):
        return self.__height
    def GetColor(self):
        return self.__framecolor
    def SetDescription(self,NewDescription):
        self.__description = NewDescription

import os
current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir,"Pictures.txt")

PicArray = []
for i in range(100):
    PicArray.append(Picture("",0,0,""))

def ReadData():
    count = 0
    
    try:
                
        if os.path.exists(file_path):
            with open(file_path,"r") as file:
                flag = True
                desc = file.readline().strip()
                width = int(file.readline())
                height = int(file.readline())
                color = file.readline().strip()
                while (flag == True):
                    PicArray[count] = Picture(desc,width,height,color)
                    count += 1
                    desc = file.readline().strip()
                    if desc != "":   
                        width = int(file.readline())
                        height = int(file.readline())
                        color = file.readline().strip()
                    else:
                        flag = False
        else:
            print("file doesnt exists")
        return count
    
    except IOError:
        print("file not found")


#----MAIN PROGRAM----
def main():
    NumberOfPics = ReadData()


    print("Please enter the requirments for a picture")
    InColor = input("enter the color of the picture ")
    InWidth = int(input("enter the Max width of the picture "))
    InHeight = int(input("enter the Min height of the picture "))
    for i in range(NumberOfPics):
        if (PicArray[i].GetColor() == InColor.lower()):
            if PicArray[i].GetWidth() <= InWidth:
                if PicArray[i].GetHeight() <= InHeight:
                    print(PicArray[i].GetDescription())
                    print(PicArray[i].GetWidth())
                    print(PicArray[i].GetHeight())

main()
'''
'''
#Q3
def AddNode(ArrayNodes,RootPointer,FreeNode):
    data = int(input("enter a data to add in the binary tree"))
    if FreeNode == 20:
        print("Tree is Full")
        return ArrayNodes, RootPointer, FreeNode
    ArrayNodes[FreeNode][1] = data
    newnode = FreeNode
    FreeNode += 1
    
    if RootPointer == -1:
        RootPointer = newnode
        return ArrayNodes, RootPointer, FreeNode
    
    #Traverse
    current = RootPointer
    while True:
        if data < ArrayNodes[current][1]: #Go left
            if ArrayNodes[current][0] == -1: #Left is empty
                ArrayNodes[current][0] = newnode
                return ArrayNodes, RootPointer, FreeNode
            else:
                current = ArrayNodes[current][0]

        else:
            if ArrayNodes[current][2] == -1:
                ArrayNodes[current][2] = newnode
                return ArrayNodes, RootPointer, FreeNode
            else:
                current = ArrayNodes[current][2]

def PrintAll():
    global ArrayNodes
    print("Left Pointer    |      Data      |  RightPointer")
    print("____________________________________________________________")
    for i in range(20):
        
        print(f"  {ArrayNodes[i][0]}    |     {ArrayNodes[i][1]}    |    {ArrayNodes[i][2]}   ")

        

def Inorder(ArrayNodes, index = 0):
    if index == -1:
        return
    Inorder(ArrayNodes,ArrayNodes[index][0]) #left
    print(ArrayNodes[index][1],end = ",") #root
    Inorder(ArrayNodes,ArrayNodes[index][2]) #right

    



#----MAIN PROGRAM----
def main():
    global ArrayNodes
    global RootPointer
    global FreeNode
    
    ArrayNodes = [[-1,-1,-1] for i in range(20)]
    RootPointer = -1 
    FreeNode = 0
    for i in range(10):
            
        ArrayNodes, RootPointer, FreeNode = AddNode(ArrayNodes,RootPointer,FreeNode)
    PrintAll()
    Inorder(ArrayNodes)


main()
'''


