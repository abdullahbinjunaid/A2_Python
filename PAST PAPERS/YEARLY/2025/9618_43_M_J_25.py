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
