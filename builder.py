class Car:
    def __init__(self):
        self.make = None
        self.model = None
        self.year = None
        self.color = None
        self.sunroof = False

    def __str__(self):
        return f"{self.year} {self.make} {self.model}, Color: {self.color}, Sunroof: {self.sunroof}"


class Builder:
    def set_make(self, make):
        pass

    def set_model(self, model):
        pass

    def set_year(self, year):
        pass

    def set_color(self, color):
        pass

    def add_sunroof(self):
        pass

    def get_car(self):
        pass


class ConcreteBuilder(Builder):
    def __init__(self):
        self.car = Car()

    def set_make(self, make):
        self.car.make = make

    def set_model(self, model):
        self.car.model = model

    def set_year(self, year):
        self.car.year = year

    def set_color(self, color):
        self.car.color = color

    def add_sunroof(self):
        self.car.sunroof = True

    def get_car(self):
        return self.car


class Director:
    def __init__(self, builder):
        self.builder = builder

    def construct_sports_car(self):
        self.builder.set_make("Toyota")
        self.builder.set_model("Supra")
        self.builder.set_year(2023)
        self.builder.set_color("Red")
        self.builder.add_sunroof()


# Example usage:
if __name__ == "__main__":
    builder = ConcreteBuilder()
    director = Director(builder)

    director.construct_sports_car()
    car = builder.get_car()
    print(car)
