class Circle():

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius**2*3
      
    def perimeter(self):
        return 2*self.radius*3

NewCircle = Circle(8)
print(NewCircle.area())
print(NewCircle.perimeter())