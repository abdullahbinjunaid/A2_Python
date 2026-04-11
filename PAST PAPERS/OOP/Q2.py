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



