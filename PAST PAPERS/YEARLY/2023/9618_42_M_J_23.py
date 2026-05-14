#Q1:
'''
Animals = []

def SortDescending():
    global Animals
    ArrayLength = len(Animals)
    Temp = ""
    for x in range(0,ArrayLength - 1):
        for y in range(0,ArrayLength - x - 1):
            if Animals[y][:1] < Animals[y+1][:1]:
                Temp = Animals[y]
                Animals[y] = Animals[y+1]
                Animals[y+1] = Temp

#----MAIN PROGRAM----
def main():
    global Animals
    Animals = ["horse","lion","rabbit","mouse","bird","deer","whale","elephant","kangaroo","tiger"]
    SortDescending()
    print(Animals)
main()
'''

#Q2
class SaleData:
    def __init__(self,ID,Quantity):
        self.__ID = ID #String
        self.__Quantity = Quantity #Integer
    #Getters
    def GetID(self):
        return self.__ID
    def GetQuantity(self):
        return self.__Quantity
    


#Global    
CircularQueue = [SaleData("",-1)]*5
Head = 0
Tail = 0
NumberOfItems = 0

def Enqueue(Data):
    global Head,Tail,NumberOfItems,CircularQueue
    #if (Head == Tail + 1) or ((Tail == len(CircularQueue) - 1) and (Head == 0)): Another condition for checking 
    
    if NumberOfItems == 5:
        print("Queue is Full")
        return -1
    elif (Tail == len(CircularQueue) - 1) and (Head != 0) :
        Tail = 0
        CircularQueue[Tail] = Data
        NumberOfItems += 1
        return 1
    else:
        Tail += 1
        CircularQueue[Tail] = Data
        NumberOfItems += 1
        return 1

    



