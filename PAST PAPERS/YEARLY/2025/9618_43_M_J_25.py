#Q1
'''
def Enqueue(Data):
    global HeadPointer
    global TailPointer
    if HeadPointer == len(Queue) - 1:
        print("The queue is full")
        return False
    if HeadPointer == -1 and TailPointer == -1:
        HeadPointer = 0
        TailPointer = 0
        Queue[HeadPointer] = Data
        print("Data stored in the queue")
        return True
    else:
        TailPointer += 1
        Queue[TailPointer] = Data
        print("Data stored in the queue")
        return True
    
def Dequeue():
    global HeadPointer
    global TailPointer
    if HeadPointer == -1 and TailPointer == -1:
        print("The queue is empty")
        return -1
    elif  HeadPointer == TailPointer:
        Data = Queue[HeadPointer]
        Queue[HeadPointer] = -1
        HeadPointer = -1
        TailPointer = -1
        print("Successful dequeue")
        return Data
    else:
        Data = Queue[HeadPointer]
        Queue[HeadPointer] = -1
        HeadPointer += 1
        print("successfull dequeue")
        return Data


import os    
def CreateQueue():
    file_path = os.path.dirname(__file__)
    file = os.path.join(file_path,"QueueData.txt")
    if os.path.exists(file):
        with open(file,"r") as f:
            for line in f:
                Value = int(line.strip())
                flag = Enqueue(Value)
                if flag == -1:
                    print("Queue Full")
    else:
        print("The file doesn't exists")
    

Queue = [-1]*50
HeadPointer = -1
TailPointer = -1
CreateQueue()
Data = Dequeue()
Total = 0
while Data != -1:
    Total += Data
    Data = Dequeue()
print(f"The total of the entire queue is {Total}")
'''
#Q2
'''
DataArray = [0,3,4,56,67,44,43,32,31,345,45,6,54]
def InserstionSort(array):
    
    for i in range(1,len(array)):
        j = i
        while (j > 0) and (array[j-1] > array[j]):
            temp = array[j]
            array[j] = array[j-1]
            array[j-1] = temp
            j = j-1
    return array

def OutPutArray(array):
    line = ""
    for i in array: 
        print(str(i) , end = " ")


OutPutArray(DataArray)
DataArray = InserstionSort(DataArray)
print("\n",end = "")
OutPutArray(DataArray)

def Search(Array , ItemToFind):
    LB = 0
    UB = len(Array) 
    found = False
    while (found == False) and (LB <= UB):
        MV = int((UB+LB)/2)
        if ItemToFind > Array[MV]:
            LB = MV + 1
        elif ItemToFind < Array[MV]:
            UB = MV - 1
        else:
            found = True
    if found == True:
        print(f"{ItemToFind} was found at index {MV}")   
        return MV
    else:
        print(f"{ItemToFind} was not found")
        return -1
    
            
print("\n", end="")        
Search(DataArray , 0)
Search(DataArray , 345)
Search(DataArray , 67)
Search(DataArray , 2)
'''
#Q3
'''
class Node:
    def __init__(self,TheData):
        self.TheData = TheData
        self.NextNode = -1
    def GetData(self):
        return self.TheData
    def GetNextNode(self):
        return self.NextNode
    def SetNextNode(self,object):
        self.NextNode = object

class LinkedList:
    def __init__(self):
        self.HeadNode = -1
    def InsertNode(self, Data):
        Node_obj = Node(Data)
        Node_obj.SetNextNode(self.HeadNode)
        self.HeadNode = Node_obj
    
    def Traverse(self):
        Line = "" 
        Current = self.HeadNode
        while Current != -1:
            Line = Line + str(Current.GetData()) + " "
            Current = Current.GetNextNode()
            print(Line)
        return Line
    def RemoveNode(self,Find):
        if self.HeadNode == -1:
            return False
            
        Current = self.HeadNode
        Previous = None
        
        while Current != -1:
            if Current.GetData() == Find:
                if Previous is None:
                    # We are removing the head node
                    self.HeadNode = Current.GetNextNode()
                else:
                    # Bypass the current node
                    Previous.SetNextNode(Current.GetNextNode())
                
                print(f"Node with data {Find} removed.")
                return True
            
            # Move to next
            Previous = Current
            Current = Current.GetNextNode()
            
        print("No such data was found.")
        return False



MyList = LinkedList()
 

MyList.InsertNode(10)
MyList.InsertNode(20)
MyList.InsertNode(30)
MyList.InsertNode(40)
MyList.InsertNode(50)
 
print(MyList.Traverse())
 

MyList.RemoveNode(30)
 
print(MyList.Traverse())
'''