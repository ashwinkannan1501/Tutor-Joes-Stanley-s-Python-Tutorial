"""
Hierarchical Inheritance  :-
-----------------------------
    When more than one derived class are created from a single base class, this type inheritance is called hierarchical
inheritance.

SYNTAX :-
-----------
                                -----------
                                | class A |
                                -----------
                                    |
                                    |
                   --------------------------------------
                   |                |                   |
                   |                |                   |
               -----------      ------------        ------------
               | class B |      | class C |         |  class D |
               -----------      -----------         ------------
"""


class Animal:
    alive = True

    def wake_up(self):
        print("All animals are waked up in the morning")

    def hunt(self):
        print("This animal is hunting")

    def eat(self):
        print("This animal is eating")

    def sleep(self):
        print("This animal is sleeping")


class Dog(Animal):
    def bark(self):
        print("The dog can bark")


class Rabbit(Animal):
    def run_fast(self):
        print("The rabit can run fast")


class Eagle(Animal):
    def fly(self):
        print("The eagle can fly")


class Fish(Animal):
    def swim(self):
        print("The fish can swim")


class Tortoise(Animal):
    def hide(self):
        print("The tortoise can hide inside the shell")


animal = Animal()
print("Is animal is alive ? : ", animal.alive)
animal.wake_up()
animal.hunt()
animal.eat()
animal.sleep()

dog = Dog()
dog.wake_up() ;dog.sleep() ; dog.bark()
print(dog.alive)