class Parent:
    def __init__(self, value):
        self.value = value



class Child(Parent):
    def __init__(self, value, extra):
        super().__init__(value)
        self.extra = extra

obj = Child(10, 20)
print(obj.value, obj.extra)

