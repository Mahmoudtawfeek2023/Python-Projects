class DriveBot:
    def __init__(self, motor_speed=0, direction=180, sensor_range=10):
        self.motor_speed = motor_speed
        self.direction = direction
        self.sensor_range = sensor_range

    def control_bot(self, new_speed, new_direction):
        self.motor_speed = new_speed
        self.direction = new_direction

    def adjust_sensor(self, new_sensor_range):
        self.sensor_range = new_sensor_range

# Ask the user for the number of robots to create
num_robots = int(input("How many robots do you want to create? "))

# Create a list of robot objects with custom parameter values
robots = []
for i in range(num_robots):
    speed = int(input(f"Enter motor speed for robot {i+1}: "))
    direction = int(input(f"Enter direction for robot {i+1}: "))
    range_ = int(input(f"Enter sensor range for robot {i+1}: "))

    robot = DriveBot(motor_speed=speed, direction=direction, sensor_range=range_)
    robots.append(robot)

# Use the control_bot and adjust_sensor methods to rotate each robot
# with the new parameter values
for robot in robots:
    new_speed = int(input("Enter new motor speed: "))
    new_direction = int(input("Enter new direction: "))
    new_range = int(input("Enter new sensor range: "))

    old_values = {
        "Motor Speed": robot.motor_speed,
        "Direction": robot.direction,
        "Sensor Range": robot.sensor_range
    }

    robot.control_bot(new_speed, new_direction)
    robot.adjust_sensor(new_range)

    new_values = {
        "Motor Speed": robot.motor_speed,
        "Direction": robot.direction,
        "Sensor Range": robot.sensor_range
    }

    # Print a comparison of the old and new instance variable values
    print(f"Robot {robots.index(robot)+1}:")
    print("{:<15} {:<15} {:<15}".format("Instance", "Old Value", "New Value"))
    print("{:-<15} {:-<15} {:-<15}".format("", "", ""))
    for key in old_values:
        print("{:<15} {:<15} {:<15}".format(key, old_values[key], new_values[key]))
    print()