# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         pass
#     def move(self):
#         print("move")

#     def draw(self):
#         print("draw")

# point = Point(10, 20)
# print(point.x)

from os import name


class Person:
    def __init__(self,name) -> None:
        self.name = name
    def talk(self):
        print(f"Hi, I am {self.name}")

john = Person("john smith")
john.talk()

bob = Person("bob smith")
bob.talk()