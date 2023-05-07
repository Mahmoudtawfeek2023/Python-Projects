# 1. Create a list of pizza toppings
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

# 2. Create a list of pizza prices
prices = [2, 6, 1, 3, 2, 7, 2]

# 3. Count the number of $2 slices
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

# 4. Get the number of pizza toppings
num_pizzas = len(toppings)

# 5. Print a message with the number of pizza toppings
print("We sell " + str(num_pizzas) + " different kinds of pizza!")

# 6. Create a two-dimensional list of pizza toppings and prices
pizza_and_prices = [[price, topping] for price, topping in zip(prices, toppings)]

# 7. Print the list of pizza toppings and prices
print(pizza_and_prices)

# 8. Sort the list of pizza toppings and prices by increasing price
pizza_and_prices.sort()

# 9. Get the cheapest pizza
cheapest_pizza = pizza_and_prices[0]

# 10. Get the most expensive pizza
priciest_pizza = pizza_and_prices[-1]

# 11. Remove the most expensive pizza
pizza_and_prices.pop()

# 12. Add a new topping to the list
pizza_and_prices.append([2.5, "peppers"])

# 13. Get the three cheapest pizzas
three_cheapest = pizza_and_prices[:3]

# 14. Print the three cheapest pizzas
print(three_cheapest)