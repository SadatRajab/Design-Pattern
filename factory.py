class Shape:
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        print("Draw Circle")

class Square(Shape):
    def draw(self):
        print("Draw Square")

class ShapeFactory:
    @staticmethod
    def create_shape(shape_type):
        if shape_type == "Circle":
            return Circle()
        elif shape_type == "Square":
            return Square()
        else:
            raise ValueError("Invalid shape type")

# Example usage:
if __name__ == "__main__":
    factory = ShapeFactory()

    circle = factory.create_shape("Circle")
    circle.draw()

    square = factory.create_shape("Square")
    square.draw()
