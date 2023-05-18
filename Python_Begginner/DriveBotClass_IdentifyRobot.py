class DriveBot:
    robot_count = 0   # class variable to keep track of the number of robots

    def __init__(self, motor_speed=0, direction=180, sensor_range=10):
        DriveBot.robot_count += 1   # increment the robot count
        self.id = DriveBot.robot_count   # assign the robot count as the robot's ID
        self.motor_speed = motor_speed
        self.direction = direction
        self.sensor_range = sensor_range
        self.latitude = None
        self.longitude = None
        self.all_disabled = None

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

# Set the latitude, longitude, and all_disabled values for each robot object
for robot in robots:
    while True:
        try:
            lat = float(input(f"Enter the latitude for robot {robot.id}: "))
            if -90 <= lat <= 90:
                robot.latitude = lat
                break
            else:
                print("The latitude must be between -90 and 90.")
        except ValueError:
            print("The latitude must be a number.")

    while True:
        try:
            lng = float(input(f"Enter the longitude for robot {robot.id}: "))
            if -180 <= lng <= 180:
                robot.longitude = lng
                break
            else:
                print("The longitude must be between -180 and 180.")
        except ValueError:
            print("The longitude must be a number.")

    while True:
        disabled = input(f"Is robot {robot.id} disabled? (y/n): ")
        if disabled.lower() == "y":
            robot.all_disabled = True
            break
        elif disabled.lower() == "n":
            robot.all_disabled = False
            break
        else:
            print("Please enter y or n.")

# Use the control_bot and adjust_sensor methods to rotate each robot
# with the new parameter values
for robot in robots:
    new_speed = int(input(f"Enter new motor speed for robot {robot.id}: "))
    new_direction = int(input(f"Enter new direction for robot {robot.id}: "))
    new_range = int(input(f"Enter new sensor range for robot {robot.id}: "))

    old_values = {
        "Motor Speed": robot.motor_speed,
        "Direction": robot.direction,
        "Sensor Range": robot.sensor_range,
        "Latitude": robot.latitude,
        "Longitude": robot.longitude,
        "All Disabled": "Yes" if robot.all_disabled else "No"
    }

    robot.control_bot(new_speed, new_direction)
    robot.adjust_sensor(new_range)

    new_values = {
        "Motor Speed": robot.motor_speed,
        "Direction": robot.direction,
        "Sensor Range": robot.sensor_range,
        "Latitude": robot.latitude,
        "Longitude": robot.longitude,
        "All Disabled": "Yes" if robot.all_disabled else "No"
    }

    # Print a comparison of the old and new instance variable values
    print(f"Robot {robot.id}:")
    print("{:<15} {:<15} {:<15}".format("Instance", "Old Value", "New Value"))
    print("{:-<15} {:-<15} {:-<15}".format("", "", ""))
    for key in old_values:
        print("{:<15} {:<15} {:<15}".format(key, old_values[key], new_values[key]))
    print()