class character():
    def __init__ (self, name):
        self.name = name
        self.__life = 3
        self.__score = 0

    def kicked(self):
        self.__score = self.__score + 10

    def punched(self):
        self.__score = self.__score + 5

    def stabbed(self):
        self.__life = self.__life - 1



    def displaylife(self):
        return self.__life
    def displayscore(self):
        return self.__score



def intro(self):
    print(f"name : {self.name}")
    print(f"life : {self.__life}")
    print(f"score:{self.__score}")


        






    
        
    
