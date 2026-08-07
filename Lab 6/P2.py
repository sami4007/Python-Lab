class Vehicle:
    def __init__(self, vehicle_name, seats):
        self.name = vehicle_name
        self.seating_capacity = seats

    def fare(self):
        fare_per_seat = 90
        return self.seating_capacity * fare_per_seat


class Bus(Vehicle):
    def fare(self):
        basic_fare = super().fare()
        maintenance_charge = basic_fare * 0.10
        return basic_fare + maintenance_charge


my_bus = Bus("College Bus", 30)

# Display the total fare
print("Total Bus Fare:", my_bus.fare())