class Rectangle:

    def set_dimensions(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width
    
    def perimeter(self):
        return 2*(self.height+self.width)
    
rectangle1 = Rectangle()
rectangle1.set_dimensions(4,3)
print("The height and width are: ",rectangle1.height,rectangle1.width)
print("The area is: ",rectangle1.area())
print("The perimeter of rectangle :",rectangle1.perimeter())
