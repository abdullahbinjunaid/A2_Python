# Q1: Answer is commented
"""
Stack = [None]*30
TopOfStack = -1

def Push(num):
    global TopOfStack
    if TopOfStack == len(Stack) - 1:
        return False
    else:
        TopOfStack += 1
        Stack[TopOfStack] = num
        return True
    
def Pop():
    global TopOfStack
    if TopOfStack == -1:
        print("Stack is empty")
        return -999
    else:
        data = Stack[TopOfStack]
        Stack[TopOfStack] = None
        TopOfStack -= 1
        print(f"The value which was popped was {data}")
        return data

def FindValues():
    data = Pop()
    max = data 
    min = data
    while data != -999:
        if data > max :
            max = data
        if data < min :
            min = data
        data = Pop()
    print(f"The largest number in the stack : {max}")
    print(f"The smallest number in the stack : {min}")



    

def main():
    import random
    Input = random.randint(0,1000)
    flag = Push(Input)
    while flag != False:
        Input = random.randint(0,1000)
        flag = Push(Input)
    print("Stack Full")
    print(Stack)
    FindValues()

main()
"""

# Q2:

