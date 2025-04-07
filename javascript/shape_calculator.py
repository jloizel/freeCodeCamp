class Rectangle:
  # Initialise the Rectangle class with __init__ method
  def __init__(self, width, height):
    self.width = width
    self.height = height

  # Format string print
  def __str__(self):
    return f"Rectangle(width={self.width}, height={self.height})"

  # Define the set_width method
  def set_width(self, width):
    self.width = width

  # Define the set_height method
  def set_height(self, height):
    self.height = height

  # Define the get_area method
  def get_area(self):
    return self.width * self.height

  # Define the get_perimeter method
  def get_perimeter(self):
    return 2 * (self.width + self.height)

  # Define the get_diagonal method
  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** 0.5

  # Define the get_picture method
  def get_picture(self):
    if (self.width > 50 or self.height > 50):
      return "Too big for picture."
    string = (("*" * self.width) + "\n") * self.height
    return string

  # Define the get_amount_inside method
  def get_amount_inside(self, shape):
    return int(self.get_area() / shape.get_area())

class Square(Rectangle): # Square class will inherit the methods from the Rectangle class (sub-class)
  # Initialise the Square class with __init__ method
  def __init__(self, side):
    self.width = side
    self.height = side

  # Format string format
  def __str__(self):
    return f"Square(side={self.width})"

  # Define the set_side method
  def set_side(self, side):
    self.width = side
    self.height = side