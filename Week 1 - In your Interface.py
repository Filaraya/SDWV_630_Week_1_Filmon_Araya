"""
Name: Filmon Araya
Week_1: In your Interface

"""

class Teams:
    def __init__(self, members):
        self.__myTeam = members
        self.index = len(members)

    def __len__(self):
        return len(self.__myTeam)
    
    # 1) Add the __contains__ protocol and show whether or not  'Tim' and 'Sam' are part of our team.
    def __contains__(self,name):
        """to check the name wheither or not in member team"""
        if name in self.__myTeam:
            return True
        else:
            return False
    
    # 2) Add the __iter__ protocol 
    def __iter__(self):
        """ to show to print each member of the classmates object. """
        return self
    
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index  = self.index - 1
        return self.__myTeam[self.index]
        
def main():
    classmates = Teams(['John', 'Steve', 'Tim'])
    # 1) Show whether or not  'Tim' and 'Sam' are part of our team.  
    print("Tim" in classmates)
    print("Sam" in classmates)

    # 2) Show how you can print each member of the classmates object.
    iter(classmates)
    for member in classmates:
        print(member) 

    # 3) To determine if the class classmates implements the __len__ method.
    print(type(classmates) is Teams)
main()

#4) Explain the difference between interfaces and implementation.
    #Interfaces cannot be instantiated, but rather are implemented.
    #A class that implements an interface must implement all of the non-default methods described in the interface.
#5)
#For all storage device, USB, Cloud and HD need a different data storage system.
#so they would all need different implementations of storing and removing data. 
