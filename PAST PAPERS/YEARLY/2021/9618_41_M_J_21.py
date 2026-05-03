#Q1
'''
class node:
    def __init__(self,Data,NextNode):
        self.Data = Data
        self.NextNode = NextNode
def OutPutNodes(List,startp):

    current = startp
    while current != -1:
        print(List[current].Data)
        current = List[current].NextNode
def AddNode(List):
    global startpointer
    global emptylist
    global startpointer
    if emptylist == -1:
        print("the linked list is full")
        return False
    else:
            
        data = int(input("enter a data that is to added in the linked list"))
        current = startpointer
        while List[current].NextNode != -1:
            current = List[current].NextNode
        temp = emptylist
        List[emptylist].Data = data
        List[current].NextNode = emptylist
        emptylist = List[emptylist].NextNode
        List[temp].NextNode = -1
        print("the node was added")
        return True



#----MAIN PROGRAM----
def main():
    #index           0        1         2           3         4
    LinkedList = [node(1,1),node(5,4),node(6,7),node(7,-1),node(2,2)
                #      5           6         7        8         9 
                   ,node(0,6),node(0,8),node(56,3),node(0,9),node(0,-1)]
    global startpointer
    global emptylist
    startpointer = 0
    emptylist = 5
    OutPutNodes(LinkedList,startpointer)
    flag = AddNode(LinkedList)
    print(flag)
    OutPutNodes(LinkedList,startpointer)
    
main()
'''