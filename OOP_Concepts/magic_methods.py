class Rectangle:
    def __init__(self, length, width):
        # initialize the rectangle with lengh and width
        self.length = length
        self.width = width
    @property
    def area(self):
        #calculating the area of the rectangle
        return self.length * self.width
    
    @property
    def perimeter(self):
        #calculate the perimeter of the rectangle
        return 2 * (self.length + self.width)
    
    def __str__(self):
        #return a string representation of the rectangle
        return f'Regtangle(Length: {self.length}, Width: {self.width})'
    
    def __eq__(self, other):
        #compare two rectangles by comparing their areas
        if isinstance(other, Rectangle):
            return self.area == other.area
        return False
    #creating two reactangle instances with different dimentions
rectangle1 = Rectangle(3, 2)
rectangle2 = Rectangle(7, 5)
    
#demonstrating the use of all methods
print(f'Rectangle 1: {rectangle1}')  #string representation
print(f'Area of Rectangle 1: {rectangle1.area}') # area
print(f'Perimeter of Rectangle 1: {rectangle1.perimeter}') # perimeter

print(f'Rectangle 2: {rectangle2}') # string
print(f'Area of Rectangle 2: {rectangle2.area}') #area
print(f'Perimeter of Rectangle 2: {rectangle2.perimeter}') # perimeter

#comparing areas of the two rectangles
print(f'Are the areas of Rectangle 1 and Rectangle 2 equal? {rectangle1 == rectangle2}')
