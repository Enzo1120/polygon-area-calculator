def get_picture(self):
      if(self.width > 50 or self.height > 50):
        return "Too big for picture."
      string = (("*" * self.width) + "\n") * self.height
      return string

    def get_area(self):
      return self.width * self.height

    def get_perimeter(self):
      return 2 * self.width + 2 * self.height

    def get_diagonal(self):
      return ((self.width ** 2 + self.height ** 2) ** .5)

    def get_amount_inside(self, shape):
      return int(self.get_area() / shape.get_area())




class Square(Rectangle):
    def __init__(self, side):
      self.width = side
      self.height = side

    def __str__(self):
      return f'Square(side={self.width})'

    def set_side(self, side):
      self.width = side
      self.height = side
