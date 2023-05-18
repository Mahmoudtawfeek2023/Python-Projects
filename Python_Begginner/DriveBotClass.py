class DriveBot:
    def __init__(self):
        self.motor_speed = 0
        self.direction = 0
        self.sensor_range = 0

robot = DriveBot()

while True:
    speed = input("Enter motor speed (press Enter to skip): ")
    if not speed:
        break
    robot.motor_speed = int(speed)

    direction = input("Enter direction (press Enter to skip): ")
    if not direction:
        break
    robot.direction = int(direction)

    range_ = input("Enter sensor range (press Enter to skip): ")
    if not range_:
        break
    robot.sensor_range = int(range_)

print("Robot - Motor Speed:", robot.motor_speed)
print("Robot - Direction:", robot.direction)
print("Robot - Sensor Range:", robot.sensor_range)