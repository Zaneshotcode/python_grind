from xmlrpc.client import Marshaller


class Mammal:
    def walk(self):
        print("walk")

class Dog(Mammal):
    def bark(self):
        print("bark")

class Cat(Mammal):
    def be_cute(self):
        print("cute")

cat1 = Cat()
cat1.be_cute()