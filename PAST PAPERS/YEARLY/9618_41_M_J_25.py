#Q1:
'''
Queue = [-1]*20
HeadPointer = -1
TailPointer = -1
NumberItems = 0

def Enqueue(data):
    global  HeadPointer
    global TailPointer
    global NumberItems

    if NumberItems == 20:
        print("Queue is full")
        return False
    elif (TailPointer == -1) and (HeadPointer == -1):
        TailPointer = 0 
        HeadPointer = 0
        Queue[TailPointer] = data
        NumberItems += 1 
        return True
    elif (TailPointer == len(Queue) - 1): #and (HeadPointer != 0):
        TailPointer = 0
        Queue[TailPointer] = data
        NumberItems += 1 
        return True
    else:
        TailPointer += 1
        Queue[TailPointer] = data
        NumberItems += 1
        return True
    
def Dequeue():
    global TailPointer
    global HeadPointer
    global NumberItems
    if NumberItems == 0:
        print("Queue is empty")
        return -1
    elif HeadPointer == TailPointer:
        Value = Queue[HeadPointer]
        TailPointer = -1
        HeadPointer = -1
        NumberItems -= 1
        return Value
    elif HeadPointer == len(Queue) - 1:
        Value = Queue[HeadPointer]
        HeadPointer = 0
        NumberItems -= 1
        return Value
    else:
        Value = Queue[HeadPointer]
        HeadPointer += 1 
        NumberItems -= 1
        return Value





for i in range(1,26):
    flag = Enqueue(i)
    if flag:
        print("Successful")
    else:
        print("Unsuccessful")

print(Dequeue())
print(Dequeue())
print(HeadPointer,TailPointer,NumberItems)
'''
        
#Q2:



def ReadData():
    Arr = []
    import os
    file_path = os.path.dirname(__file__)

    f = input("enter a file name to be read ")
    print(f)
    filename = os.path.join(file_path, f)
    
    with open(filename,"r") as file:
        value = file.readline().strip()
        
        while value != "":
            Arr.append(value)
            value = file.readline().strip()
    
    return Arr

arr = ReadData() 

def SplitData(DataArray):
    Red = []
    Blue = []
    Green = []
    Orange = []
    Pink = []
    Yellow = []
    for i in DataArray:
        count = 0 
        while i[count] != ",":
            count += 1
        V1 = i[:count]
        V2 = i[count + 1:]
        match V2:
            case "red":
                Red.append(V1)
            case "blue":
                Blue.append(V1)
            case "green":
                Green.append(V1)
            case "orange":
                Orange.append(V1)
            case "pink":
                Pink.append(V1)
            case "yellow":
                Yellow.append(V1)
            
    print(Red)                                
    print(Blue)                                
    print(Green)                                
    print(Orange)                                
    print(Pink)                                
    print(Yellow)                                

SplitData(arr)