class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change):
        new_speed = self.current_speed + speed_change
        if new_speed < 0:
            self.current_speed = 0
        elif new_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        else:
            self.current_speed = new_speed

    def drive(self, hours):
        distance = self.current_speed * hours
        self.travelled_distance += distance

# Main program
if __name__ == "__main__":
    car = Car("ABC-123", 142)
    car.accelerate(30)
    car.accelerate(70)
    car.accelerate(50)
    print("Current Speed:", car.current_speed, "km/h")
    car.accelerate(-200)
    print("Final Speed:", car.current_speed, "km/h")

    car.travelled_distance = 2000
    car.current_speed = 60
    car.drive(1.5)
    print("Travelled Distance:", car.travelled_distance, "km")
