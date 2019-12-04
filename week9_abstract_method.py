# Python program showing 
# abstract class cannot 
# be an instantiation 
from abc import ABC,abstractmethod 
  
class Animal(ABC): 
    @abstractmethod
    def move(self): 
        pass
class Human(Animal): 
    def move(self): 
        print("I can walk and run") 
  
class Snake(Animal): 
    def move(self): 
        print("I can crawl") 
  
class Dog(Animal): 
    def move(self): 
        print("I can bark") 
  
class Lion(Animal): 
    def move(self): 
        print("I can roar") 
  
species1=Human()
species2=Snake()
species3=Lion()
species4=Dog()

species1.move()
species2.move()
species3.move()
species4.move()