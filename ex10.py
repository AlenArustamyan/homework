#Create a Python class representing a car with methods for accelerating and braking.


class Car:
    def __init__(self, make, model, year, speed=0):
        self.make = make
        self.model = model
        self.year = year
        self.speed = speed

    def accelerate(self, acceleration_rate):
        if acceleration_rate > 0:
            self.speed += acceleration_rate
            print(f"The car is accelerating. Current speed: {self.speed} km/h")
        else:
            print("Invalid acceleration rate.")

    def brake(self, braking_rate):
        if braking_rate > 0 and braking_rate <= self.speed:
            self.speed -= braking_rate
            print(f"The car is braking. Current speed: {self.speed} km/h")
        elif braking_rate > 0 and braking_rate > self.speed:
            self.speed = 0
            print("The car has come to a complete stop.")
        else:
            print("Invalid braking.")

my_car = Car(make="Toyota", model="Camry", year=2022)
my_car.accelerate(20)
my_car.brake(10)
my_car.accelerate(30)
my_car.brake(50)

