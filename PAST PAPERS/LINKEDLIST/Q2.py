class node:
    def __init__(self, data, nextnode):
        self.data = data
        self.nextnode = nextnode

#Index     =    0            1          2          3            4          5         6          7           8          9   
LinkedList = [node(1,1), node(5,4), node(6,7), node(7,-1), node(2,2), node(0,6), node(0,8), node(58,3), node(0,9), node(0,-1)]

def outputNodes(startpointer):
    Next = startpointer
    print(f"Index : {Next}  |  Data : {LinkedList[Next].data}  |  Next Node : {LinkedList[Next].nextnode}")
    Ncount = 1
    while LinkedList[Next].nextnode != -1:
        Next = LinkedList[Next].nextnode
        print(f"Index : {Next}  |  Data : {LinkedList[Next].data}  |  Next Node : {LinkedList[Next].nextnode}")
        Ncount += 1
    print(Ncount)

def addNode(LinkedList, startpointer):
    global emptylist
    dataInput = int(input("enter a data to add in the linked list"))
    outputNodes(startpointer)
    if emptylist == -1:
        return False
    next = startpointer
    while (LinkedList[next].nextnode != -1):
        next = LinkedList[next].nextnode
    
    LinkedList[next].nextnode = emptylist
    emptylist = LinkedList[emptylist].nextnode
    next = LinkedList[next].nextnode
    LinkedList[next].data = dataInput
    LinkedList[next].nextnode = -1
    outputNodes(startpointer)

    return True













def main():
    startpointer = 0
    emptylist = 5
    outputNodes(startpointer)
    addNode(LinkedList,startpointer, emptylist)


main()