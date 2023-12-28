from abc import ABCMeta, abstractclassmethod

class Animal(metaclass=ABCMeta):
    def __init__(self, name) -> None:
        self.name = name

    @abstractclassmethod
    def cry(self):
        pass

class Dog(Animal):
    def __init__(self) -> None:
        super().__init__("dog")

    def cry(self):
        print("{} :汪汪~".format(self.name))

class Cat(Animal):
    def __init__(self) -> None:
        super().__init__("cat")

    def cry(self):
        print("{} :喵喵~".format(self.name))

class Sheep(Animal):
    def __init__(self) -> None:
        super().__init__("sheep")

    def cry(self):
        print("{} :咩咩~".format(self.name))

class Cow(Animal):
    def __init__(self) -> None:
        super().__init__("cow")

    def cry(self):
        print("{} :哞哞~".format(self.name))

if __name__ == '__main__':
    # 测试代码
    animal = Dog()
    animal.cry()

    animal = Cat()
    animal.cry()

    animal = Sheep()
    animal.cry()

    animal = Cow()
    animal.cry()
