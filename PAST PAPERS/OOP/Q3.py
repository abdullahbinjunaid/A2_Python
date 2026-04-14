class Balloon:
    def __init__(self, Colour, DefenceItem):
        self.__Health = 100
        self.__Colour = Colour
        self.__DefenceItem = DefenceItem
        
    def GetDefenceItem(self):
        return self.__DefenceItem
    def ChangeHealth(self, value):
        self.__Health += value
        if (self.__Health <= 0):
            return True
        else:
            return False
        
def Defend(BalloonObj):
    strength = int(input("enter the strength of the oponent "))
    flag = BalloonObj.ChangeHealth(strength)
    print(BalloonObj.GetDefenceItem())
    if flag == False:
        print("there is health remaining of the balloon")
    else:
        print("no health is left of the balloon ")
        
def main():
    defence = (input("enter the defence item for balloon "))
    color = (input("enter the COLOR balloon "))
    Balloon1 = Balloon(color.lower(),defence.lower())
    Defend(Balloon1)

main()