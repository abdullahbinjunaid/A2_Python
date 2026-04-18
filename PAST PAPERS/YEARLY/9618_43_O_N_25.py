class BoardObject:
    def __init__(self,Code,Value):
        self.Code = Code #String
        self.Value = Value #Integer
    def GetCode(self):
        return self.Code
    def GetValue(self):
        return self.Value
    
Object1 = BoardObject("A",2) 
Object2 = BoardObject("B",3)
Object3 = BoardObject("C",5)
Object4 = BoardObject("D",2)
Object5 = BoardObject("E",7)

class Board:
    def __init__(self):
                         #Object                 #ROW              #COLUMN 
        self.TheBoard = [[Board("-",0) for i in range(10)] for i in range(10)]
    def GetObject(self,row,col):
        return self.TheBoard[row][col]
    def SetObject(self,BoardObj,Row,Col):
        self.TheBoard[Row][Col] = BoardObj