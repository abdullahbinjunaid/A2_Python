import os
DataArray = []

def main():
    with open("Data.txt","r") as file:
        for i in range(25):
            content = int(file.readline())
            DataArray.append(content)
    print(DataArray)

main()    
