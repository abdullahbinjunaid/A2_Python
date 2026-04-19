# Q1
'''
class BoardObject:
    def __init__(self,Code,Value):
        self.Code = Code #String
        self.Value = Value #Integer
    def GetCode(self):
        return self.Code
    def GetValue(self):
        return self.Value
    


class Board:
    def __init__(self):
                         #Object                 #ROW              #COLUMN 
        self.TheBoard = [[BoardObject("-",0) for i in range(10)] for i in range(10)]
    def GetObject(self,row,col):
        return self.TheBoard[row][col]
    def SetObject(self,BoardObj,Row,Col):
        self.TheBoard[Row][Col] = BoardObj
    def DisplayBoard(self):
        for row in range(10):
            for col in range(10):
                print(self.TheBoard[row][col].Code , end=" ")
            print("\n",end = "")

def main(): 
    Object1 = BoardObject("A",2) 
    Object2 = BoardObject("B",3)
    Object3 = BoardObject("C",5)
    Object4 = BoardObject("D",2)
    Object5 = BoardObject("E",7)
    GameBoard = Board()
    GameBoard.TheBoard[0][0] = Object1
    GameBoard.TheBoard[9][9] = Object2
    GameBoard.TheBoard[4][5] = Object3
    GameBoard.TheBoard[2][2] = Object4
    GameBoard.TheBoard[8][7] = Object5
    GameBoard.DisplayBoard()

    row = int(input("enter a row position between 0 and 9 "))
    while (row<0) or (row>9):
        print("invalid range for row please reenter between 0 and 9 ")
        row = int(input("enter a row position between 0 and 9 "))
    
    col = int(input("enter a column position between 0 and 9 "))
    while (col<0) or (col>9):
        print("invalid range for column please reenter between 0 and 9 ")
        col = int(input("enter a column position between 0 and 9 "))
        
    Value1 = GameBoard.TheBoard[row][col].GetCode()
    Value2 = GameBoard.TheBoard[row][col].GetValue()
    if Value1 == "-" and Value2 == 0:
        print("Miss")
    else:
        print(f"The Code is {Value1} | The Value is {Value2}")

main()
'''

#Q2


'''
Queue = [""]*100
QueueHead = -1
QueueTail = -1
NumberItems = 0

def Enqueue(Data):
    global QueueHead
    global QueueTail
    global NumberItems
    if QueueTail == len(Queue) - 1:
        return False #Queue is full
    else:
        if QueueHead == -1:
            QueueHead += 1
        QueueTail +=1
        Queue[QueueTail] = Data
        NumberItems += 1
        return True
    
def Dequeue():
    global QueueHead
    global QueueTail
    global NumberItems
    if QueueHead == -1 and QueueTail == -1:
        print("The Queue is empty")
        return "False"
    elif QueueHead == QueueTail:
        Value = Queue[QueueHead]
        QueueHead = -1
        QueueTail = -1
        return Value
    else:
        Value = Queue[QueueHead]
        QueueHead += 1
        return Value
    
def ReadData():
    import os
    file_path = os.path.dirname(__file__)
    file = os.path.join(file_path,"BinaryData.txt")
    with open(file) as f:
        data = f.readline().strip()
        while data != "":
            Enqueue(data)
            data = f.readline().strip()

def Compress():
    NewString = ""
    value = Dequeue()
    Vcount = 1
    while value != "False":
        OldValue = value
        value = Dequeue()
        if value == OldValue:
            Vcount += 1 
        else:
            NewString += OldValue + str(Vcount)
            Vcount = 1
    
    return NewString


def main():
    ReadData()
    NewString = Compress()
    print(NewString)

main()
'''



#Q3
"""
array = [None]*10

def RecursiveCount(ArrayCopy, NumberElements, DataToFind):
    if NumberElements == 0:                         # base case: no elements left
        return 0
    elif ArrayCopy[0] == DataToFind:                # first element matches
        return 1 + RecursiveCount(ArrayCopy[1:], NumberElements - 1, DataToFind)
    else:                                           # first element does not match
        return RecursiveCount(ArrayCopy[1:], NumberElements - 1, DataToFind)
    


def SplitData(Data):
    Result      = [""] * 4      # array to store 4 statements
    Index       = 0             # current position in Result
    CurrentWord = ""            # builds up each statement character by character
 
    for char in Data:
        if char == ";":                     # semicolon marks end of a statement
            Result[Index] = CurrentWord     # store completed statement
            Index += 1
            CurrentWord = ""                # reset for next statement
        else:
            CurrentWord += char             # keep building current statement
 
    return Result

IntArray = [0, 5, 1, 2, 5, 9, 9, 6, 5, 0]
 
Count = RecursiveCount(IntArray, 10, 0)
print("Count of 0s found:", Count)
 
# ── Part 3(b)(i) ── Store the string 
CodeString = "x=0;y=1;x=x+y;y++;"
 
# ── Part 3(b)(iii) ── Call SplitData() and output each element
SplitArray = SplitData(CodeString)
for line in SplitArray:
    print(line)

"""