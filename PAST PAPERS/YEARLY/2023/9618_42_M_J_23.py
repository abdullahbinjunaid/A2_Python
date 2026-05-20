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
    



def Enqueue(Data):
    global Head,Tail,NumberOfItems,CircularQueue
    #if (Head == Tail + 1) or ((Tail == len(CircularQueue) - 1) and (Head == 0)): Another condition for checking 
    
    if NumberOfItems == 5:
        print("Queue is Full")
        return -1
    elif (Tail == len(CircularQueue) - 1):
        CircularQueue[Tail] = Data
        Tail = 0
        NumberOfItems += 1
        return 1
    else:
        CircularQueue[Tail] = Data
        Tail += 1
        NumberOfItems += 1
        return 1

def Dequeue():
    global Head,Tail,NumberOfItems,CircularQueue
    if NumberOfItems == 0:
        print("The queue is empty")
        return None
    elif Head == Tail:
        Record = CircularQueue[Head]
        CircularQueue[Head] = SaleData("",-1)
        NumberOfItems -= 1
        Head = 0
        Tail = 0
        return Record
    elif Head == len(CircularQueue) - 1:
        Record = CircularQueue[Head]
        CircularQueue[Head] = SaleData("",-1)
        NumberOfItems -= 1
        Head = 0
        return Record
    else:
        Record = CircularQueue[Head]
        CircularQueue[Head] = None
        NumberOfItems -= 1
        Head += 1
        return Record
    

def EnterRecord():
    global Head,Tail,NumberOfItems,CircularQueue
    Id = input("Enter a Sale ID")
    Quantity = int(input("enter a quantity of the sale id"))
    RecordObject = SaleData(Id,Quantity)
    flag = Enqueue(RecordObject)
    if flag == -1:
        print("Full")
    else:
        print("Successful")


#Global    
CircularQueue = [SaleData("",-1)]*5
Head = 0
Tail = 0
NumberOfItems = 0

for i in range(6):
    EnterRecord()

record = Dequeue()

if record == None:
    print("error")
else:
    print(record.GetID(),record.GetQuantity())

EnterRecord()


print("\n--- Printing Queue ---")
Index = Head
for i in range(NumberOfItems):
    print(CircularQueue[Index].GetID(), CircularQueue[Index].GetQuantity())
    Index += 1
    if Index == 5: # Manual wrap-around for the print pointer
        Index = 0
'''

#Q3
'''
class Employee:
    def __init__(self,HourlyPay,EmployeeNumber,JobTitle):
        self.HourlyPay = HourlyPay #float
        self.EmployeeNumber = EmployeeNumber #String
        self.JobTitle = JobTitle #String
        self.PayYear2022 = [0.0 for i in range(52)] #Array of datatype float
    def GetEmployeeNumber(self):
        return self.EmployeeNumber
    def SetPay(self,WeekNumber,Hoursworked):
        pay = self.HourlyPay * Hoursworked
        self.PayYear2022[WeekNumber] = pay 
    def GetTotalPay(self):
        Total = 0.0
        for i in self.PayYear2022:
            Total += i
        return Total
#Child Class
class Manager(Employee):
    def __init__(self, HourlyPay, EmployeeNumber, JobTitle,BonusValue):
        super().__init__(HourlyPay, EmployeeNumber, JobTitle)
        self.BonusValue = BonusValue
    def SetPay(self,WeekNumber,Hoursworked):
        Hoursworked = (1 + self.BonusValue/100) * Hoursworked
        super().SetPay(WeekNumber,Hoursworked)

#File pathing 
import os
file_path = os.path.dirname(__file__)
file1= os.path.join(file_path,"Employees.txt")



EmployeeArray = [None]*8
if os.path.exists(file1):
    with open(file1,"r") as f:
        pay = 0.0
        Id = "" 
        Bonus = 0.0 
        Title = "" 
        Temp = "" # For checking if employee is a manager or not
        for i in range(8):
            pay = float(f.readline().strip())
            Id = f.readline().strip()
            Temp = f.readline().strip()
            try:
                Bonus = float(Temp)
                Title = f.readline().strip()
                EmployeeArray[i] = Manager(pay,Id,Title,Bonus)
            except:
                Title = f.readline().strip()
                EmployeeArray[i] = Employee(pay,Id,Title)
else:
    print("The file doesn't exists")

def EnterHours():
    file_path = os.path.dirname(__file__)
    file2 = os.path.join(file_path,"HoursWeek1.txt")
    if os.path.exists(file2):
        with open(file2,"r") as f:
            for i in range(8):
                EmployeeID = f.readline()
                Bonus = float(f.readline())
                for j in range(8):
                    if EmployeeArray[j].GetEmployeeNumber() == EmployeeID:
                        EmployeeArray[j].SetPay(1,Bonus)

    else:
        print("The file doesn't exists")



EnterHours()
for Y in range(0, 8):
    print(EmployeeArray[Y].GetEmployeeNumber(), " ", EmployeeArray[Y].GetTotalPay())
'''