class Vehicle:
    def __init__(self, make, model, amount):
        self.make = make
        self.model = model
        self.amount = amount

    def get_info(self):
        return self.make, self.model

    def get_back(self):
        return self.amount


class Car(Vehicle):
    def __init__(self, make, model, amount, fuel_type):
        super().__init__(make, model, amount)
        self.fuel_type = fuel_type

    def get_info(self):
        return self.make, self.model, self.fuel_type

    def ride(self, km):
        self.amount -= km * 7 /100



if __name__ == '__main__':
    car = Car('Mercedes', 'Benz', 100, 'Petrol')
    print(car.ride(100))
    print(car.get_back())
    print(car.get_info())