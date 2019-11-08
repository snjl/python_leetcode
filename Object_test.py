class Animal(object):
    def __init__(self, name):
        self.name = name

    def cry(self):
        print("my name is {}".format(self.name))

    def animal(self):
        print("bilibili biubiu")
        # 如果是继承类的对象，并且继承类覆盖了该方法，则会调用继承类的方法
        self.cry()


class Dog(Animal):

    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def cry(self):
        print("my name is {},age is {}".format(self.name, self.age))


d = Dog('dog', 23)
d.animal()
