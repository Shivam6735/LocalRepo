# Special function that gets invoked every time an object is created for that class.

# SYNTAX:
# class ClassName:
#     def__init__(self, parameter1, parameter2,...):
#     # initialize instance variables(attributes) here



class Rectangle:
    def __init__(self,height,width):
        print("A rectangle is created with height:{height} and width : {width}")
        self.height = height
        self.width = width




    def set_dimensions(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width
    
    def perimeter(self):
        return 2*(self.height+self.width)
    
rectangle1 = Rectangle(4,3)
rectangle1 = Rectangle(5,6)
rectangle1 = Rectangle(8,7)
# rectangle1.set_dimensions(4,3)
# print("The height and width are: ",rectangle1.height,rectangle1.width)
# print("The area is: ",rectangle1.area())
# print("The perimeter of rectangle :",rectangle1.perimeter())
