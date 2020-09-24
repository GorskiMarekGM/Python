class Point():
    def __init__(self, x,y):
        self.x = x
        self.y = y

p = Point(2,8)
print(p.x)
print(p.y)

class Car():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self,name):
        if not self.free_seats():
            return False
        self.passengers.append(name)
        return True
    
    def free_seats(self):
        return self.capacity - len(self.passengers)

car = Car(4)

people = ["Tom", "Bob", "Danny", "Ewa", "Jack"]
for person in people:
    success = car.add_passenger(person)
    if success:
        print(f"Added {person} to car")
    else: 
        print(f"no available seats for {person}")