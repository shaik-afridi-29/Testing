class Car:

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car: {self.year} {self.brand} {self.model}")
    
    def start(self):
        print(f"The {self.brand} {self.model} is starting.")

    def stop(self):
        print(f"The {self.brand} {self.model} is stopping.")

my_car = Car("Toyota", "Camry", 2021)

my_car.display_info()
my_car.start()
my_car.stop()

print("CHANGED CODE, FOR THIRD COMMIT")
print("For git diff")