#Create a Bus child class that inherits from the Vehicle claas. The default fare charge of any vehicle is seating capacity*100. if Vehicle is Bus instance, we need to add an extra 10% on full fare as a maintainance charge.So total fare for bus instance will become the final amount = total fare +10% of the total fare.



class Vehicle:
    def __init__(self,seating_capacity):
        self.seating_capacity = seating_capacity
        print("It is the main class")

    def get_fare(self):
       return self.seating_capacity * 100

class Bus(Vehicle):
    def __init__(self,seating_capacity):
     super().__init__(seating_capacity)

    def get_fare(self):
       vehicle_fare = super().get_fare()
       maintainance_fare = 0.1*vehicle_fare
       total_fare = vehicle_fare + maintainance_fare
       return total_fare
    
vehicle1 = Vehicle(50)
print("vehicle fare:",vehicle1.get_fare())

bus1 = Bus(50)
print("Bus fare:",bus1.get_fare())
   