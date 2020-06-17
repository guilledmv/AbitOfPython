class Car():
    # We create a build method
    def __init__(self):
        self.__brand = "bmw"
        self.__wheels = 4
        self.__cv = 190
        self.__started = False
    # Method which returns if this car was started
    def start(self,aux):
        self.__started = aux
        if(self.__started):
            return True
        else:
            return False
    # Method which prints an attributes of our object
    def state(self,aux22):
        print("Brand's car is : ",self.__brand," quantity of wheels : ",self.__wheels," Started : ",self.start(aux22))

car1 = Car()
aux2 = car1.start(True)
car1.state(aux2)

print("----------- We are gonna create another car-------------")
car2 = Car()
aux3 = car2.start(False)
car2.state(aux3)