# Task 1
def f_to_c(f_temp):
    c_temp = (f_temp - 32) * 5/9
    return c_temp

# Task 2
f100_in_celsius = f_to_c(100)
print(f100_in_celsius)

# Task 3
def c_to_f(c_temp):
    f_temp = c_temp * (9/5) + 32
    return f_temp

# Task 4
c0_in_fahrenheit = c_to_f(0)
print(c0_in_fahrenheit)

# Task 5
def get_force(mass, acceleration):
    return mass * acceleration

# Task 6
train_mass = 22680
train_acceleration = 10
train_force = get_force(train_mass, train_acceleration)
print(train_force)

# Task 7
print("The GE train supplies " + str(train_force) + " Newtons of force.")

# Task 8
def get_energy(mass, c=3*10**8):
    return mass * c**2

# Task 9
bomb_mass = 1
bomb_energy = get_energy(bomb_mass)
print(bomb_energy)

# Task 10
print("A 1kg bomb supplies " + str(bomb_energy) + " Joules.")

# Task 11
def get_work(mass, acceleration, distance):
    force = get_force(mass, acceleration)
    return force * distance

# Task 12
train_distance = 100
train_work = get_work(train_mass, train_acceleration, train_distance)
print(train_work)

# Task 13
print("The GE train does " + str(train_work) + " Joules of work over " + str(train_distance) + " meters.")