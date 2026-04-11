class TreasureChest:
    def __init__(self,question,answer,points):
        self.question = question #declare question
        self.answer = answer #declare answer
        self.points = points #declare points
    def getQuestion(self):
        return self.question
    def checkAnswer(self,answer):
        if self.answer == answer:
            return True
        else:
            return False
    def getPoints(self,attempts):
        match attempts:
            case attempts if attempts == 1:
                return self.points
            case attempts if attempts == 2:
                return int(self.points/2)
            case attempts if attempts == 3 or attempts == 4:
                return int(self.points/4)
            case _:
                return 0
  

                                


import os
current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, "TreasureChestData.txt")

arrayTreasure = []
def readData():
    import os  
    if os.path.exists(file_path):
        with open(file_path,"r") as file:
            for i in range(5):
                content1 = file.readline().strip()
                content2 = int(file.readline().strip())
                content3 = int(file.readline().strip())
                arrayTreasure.append(TreasureChest(content1,content2,content3))
            
    else:
        print("file does'nt exists")

   


def main():
    readData() 
    try:    
        choice =  int(input("enter a question number between 1 and 5 "))
        while choice>5 or choice<1:
            print("the question number is out of range, please renenter")
            choice =  int(input("enter a question number between 1 and 5 "))

        choice -= 1
        print(f"{arrayTreasure[choice].question} is the question ")
        ans = int(input("enter your answer for the question "))
        check = arrayTreasure[choice].checkAnswer(ans)
        attempts = 1
        while (check != True):
            print("the answer is incorrect please reenter the answer ")
            attempts += 1
            ans = int(input("enter your answer for the question "))
            check = arrayTreasure[choice].checkAnswer(ans)
        points = arrayTreasure[choice].getPoints(attempts)
        print(f"{points} are the number of points awarded to user")
    except ValueError:
        print("incorrect value entered")
    else:
        print(points)
    finally:
        print("program completed")



main()
