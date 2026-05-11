#Q1
def Unknown(x,y):
    if x < y:
        print(x + y)
        return Unknown(x+1,y) * 2
    else:
        if x == y:
            return 1
        else:
            print(x + y)
            return Unknown(x-1,y) // 2
        
def main():
    pass