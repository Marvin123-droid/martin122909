class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__('Car')
        self.brand = brand
        self.model = model

class Bike(Vehicle):
    def __init__(self, brand, model):
        super().__init__('Bike')
        self.brand = brand
        self.model = model

class Scooter(Vehicle):
    def __init__(self, brand, model):
        super().__init__('Scooter')
        self.brand = brand
        self.model = model

class RentalDetails:
    def __init__(self, duration, insurance_included):
        self.duration = duration
        self.insurance_included = insurance_included

class VehicleRentalService:
    def rent_vehicle(self, vehicle, rental_details):
        # Generic method to rent any type of vehicle
        print(f"Renting a {vehicle.vehicle_type} - {vehicle.brand} {vehicle.model} for {rental_details.duration} days.")
        if rental_details.insurance_included:
            print("Insurance is included.")

    def rent_car(self, car, rental_details):
        # Method to rent a car
        self.rent_vehicle(car, rental_details)

    def rent_bike(self, bike, rental_details):
        # Method to rent a bike
        self.rent_vehicle(bike, rental_details)

    def rent_scooter(self, scooter, rental_details):
        # Method to rent a scooter
        self.rent_vehicle(scooter, rental_details)


# Example usage:
car = Car('Toyota', 'Camry')
bike = Bike('Honda', 'CBR500R')
scooter = Scooter('Vespa', 'GTS 300')

rental_service = VehicleRentalService()

car_rental_details = RentalDetails(duration=5, insurance_included=True)
rental_service.rent_car(car, car_rental_details)

bike_rental_details = RentalDetails(duration=3, insurance_included=False)
rental_service.rent_bike(bike, bike_rental_details)

scooter_rental_details = RentalDetails(duration=7, insurance_included=True)
rental_service.rent_scooter(scooter, scooter_rental_details)
