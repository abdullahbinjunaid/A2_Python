# Q1
'''
import os
def ReadData():
    array = []
    
    file_path = os.path.dirname(__file__)
    file = os.path.join(file_path,"Data.txt")
    if os.path.exists(file):
        with open(file,"r") as f:
            for line in f:
                line = line.strip()
                array.append(line)
    else:
        print("The file does not exists")

    return array

def FormatArray(array):
    newstring = "" 
    for i in array:
        newstring = newstring + i + " "
    return newstring

def CompareStrings(str1,str2):
    len1 = len(str1)
    len2 = len(str2)
    if len1 < len2:
        for i in range(len1):
            if str1[i] > str2[i]:
                return 1
            elif str2[i] > str1[i]:
                return 2
    else:
        for i in range(len2):
            if str1[i] > str2[i]:
                return 1
            elif str2[i] > str1[i]:
                return 2



def BubbleSort(Array):
    
    top = len(Array) -1
    swap = True
    while (top > 0) and (swap == True):
        swap = False   
        for i in range(top):
            if (CompareStrings(Array[i],Array[i+1]) == 1):
                temp = Array[i]
                Array[i] = Array[i+1]
                Array[i+1] = temp
                swap = True
        top -= 1
    return Array




def main():
    Array = ReadData()
    Line = FormatArray(Array)
    print(Line)
    SortedList = BubbleSort(Array)
    Line = FormatArray(SortedList)
    print("\n", end="")
    print(Line)


main()
'''


#Q2
'''
class Horse:
    def __init__(self, Name , MaxFenceHeight, PercentageSuccess):
        self.Name = Name
        self.MaxFenceHeight = MaxFenceHeight
        self.PercentageSuccess = PercentageSuccess
    def GetName(self):
        return self.Name
    def GetMaxHeight(self):
        return self.MaxFenceHeight
    def Success(self,Height,Risk):
        if Height>self.MaxFenceHeight:
            return 20
        else:
           match Risk:
               case Risk if Risk == 1:
                   return self.PercentageSuccess * 1.0
               case Risk if Risk == 2:
                   return self.PercentageSuccess * 0.9
               case Risk if Risk == 3:
                   return self.PercentageSuccess * 0.8
               case Risk if Risk == 4:
                   return self.PercentageSuccess * 0.7
               case Risk if Risk == 5:
                   return self.PercentageSuccess * 0.6
                
    
class Fence:
    def __init__(self, Height, Risk):
        self.Height = Height
        self.Risk = Risk
    def Getheight(self):
        return self.Height
    def GetRisk(self):
        return self.Risk    

Horses = []
Horses.append(Horse("Beauty", 150, 72))
Horses.append(Horse("Jet", 160, 65))
Name = Horses[0].GetName()
print(Name)
Name = Horses[1].GetName()
print(Name)



Courses = []
for i in range(4):
    
    Iheight = int(input("enter the height of the fence b/w 70 and 180: "))
    while Iheight < 70 or Iheight > 180:
        print("input of height is out of range")
        Iheight = int(input("enter the height of the fence b/w 70 and 180: "))
    
    Irisk = int(input("enter risk which is between 1 and 5: "))
    while Irisk < 1 or Irisk > 5:
        print("input of risk is out of range")
        Irisk = int(input("enter risk which is between 1 and 5: "))
    
    Courses.append(Fence(Iheight,Irisk))    
TSuccess = 0


for i in range(2):
    TSuccess = 0
    Name = Horses[i].GetName()
    for j in range(4):

        Psuccess = Horses[i].Success(Courses[j].Height, Courses[j].Risk)
        TSuccess = TSuccess + Psuccess
        print(f"The horse {Name} at fence {j+1} has {Psuccess}% chance of success.")
    
    print(f"The Horse {Name} has an average {int(TSuccess/4)}% chance of jumping over all four fences")


'''

'''
#Q3
def InsertData():
    global LinkedList
    global FirstEmpty
    global FirstNode
    for i in range(5):
        if FirstEmpty == 20:
            print("Linked List is full can not insert data")
            return
        else:    
            data = int(input("enter a data to insert in the linked list"))
            LinkedList[FirstEmpty][0] = data
            LinkedList[FirstEmpty][1] = FirstNode
            FirstNode = FirstEmpty
            FirstEmpty += 1
    return

def OutPutLinkedList():
    global LinkedList
    global FirstEmpty
    global FirstNode
    if FirstNode == -1:                             
        print("List is empty")
        return
    current = FirstNode
    while current != -1:                            
        print(LinkedList[current][0])
        current = LinkedList[current][1]
    
def RemoveData(Find):

    global LinkedList
    global FirstEmpty
    global FirstNode
    if FirstNode == -1:
        print("Linked List is empty")
        return
    else:
        if LinkedList[FirstNode][0] == Find:
            previous = FirstNode
            FirstNode = LinkedList[FirstNode][1]
            LinkedList[previous][1] = -1
            return
        
        current = FirstNode
        while current != -1 and LinkedList[current][0] != Find:
            previous = current
            current = LinkedList[current][1]
        if current == -1:
            print("Data was not found")
            return -1
    
        LinkedList[previous][1] = LinkedList[current][1]
        LinkedList[current][1] = -1






#---- MAIN PROGRAM ----
def main():
    global LinkedList
    global FirstEmpty
    global FirstNode
    LinkedList = [[-1,-1]for i in range(20)]
    FirstEmpty = 0 
    FirstNode = -1
    InsertData()
    OutPutLinkedList()
    RemoveData(22)
    print("After")
    OutPutLinkedList()
main()

'''