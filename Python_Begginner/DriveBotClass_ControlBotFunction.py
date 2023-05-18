class DriveBot:
    def __init__(self):
        self.motor_speed = 0
        self.direction = 0
        self.sensor_range = 0

    def control_bot(self, new_speed, new_direction):
        self.motor_speed = new_speed
        self.direction = new_direction

    def adjust_sensor(self, new_sensor_range):
        self.sensor_range = new_sensor_range

robot = DriveBot()

# Ask the user to input values for the instance variables of the robot object
speed = input("Enter motor speed: ")
robot.motor_speed = int(speed)

direction = input("Enter direction: ")
robot.direction = int(direction)

range_ = input("Enter sensor range: ")
robot.sensor_range = int(range_)

# Use the control_bot and adjust_sensor methods to rotate the robot
# with the user-defined parameter values
new_speed = input("Enter new motor speed: ")
new_direction = input("Enter new direction: ")
new_range = input("Enter new sensor range: ")

old_values = {
    "Motor Speed": robot.motor_speed,
    "Direction": robot.direction,
    "Sensor Range": robot.sensor_range
}

robot.control_bot(int(new_speed), int(new_direction))
robot.adjust_sensor(int(new_range))

new_values = {
    "Motor Speed": robot.motor_speed,
    "Direction": robot.direction,
    "Sensor Range": robot.sensor_range
}

# Print a comparison of the old and new instance variable values
print("{:<15} {:<15} {:<15}".format("Instance", "Old Value", "New Value"))
print("{:-<15} {:-<15} {:-<15}".format("", "", ""))
for key in old_values:
    print("{:<15} {:<15} {:<15}".format(key, old_values[key], new_values[key]))