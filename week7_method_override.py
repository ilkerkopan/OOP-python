class Parent(object):
    def __init__(self):
        self.value = 5

    def get_value(self):
        return self.value

class Child(Parent):
    def get_value(self):
        return self.value + 1

parent1 = Parent()
print(f'parent1 has value: {parent1.get_value()}')
child1 = Child()
print(f'parent1 has value: {child1.get_value()}')