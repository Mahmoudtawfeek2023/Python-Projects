# Define the hairstyles, prices, and last_week lists
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
prices = [30, 25, 40, 20, 20, 35, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# Calculate the average price of a haircut
total_price = 0
for price in prices:
  total_price += price
average_price = total_price / len(prices)
print("Average Haircut Price: {}".format(average_price))

# Reduce all prices by $5
new_prices = [price - 5 for price in prices]
print(new_prices)

# Calculate the total revenue for last week
total_revenue = 0
for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]
print("Total Revenue: {}".format(total_revenue))

# Calculate the average daily revenue for last week
average_daily_revenue = total_revenue / 7
print("Average Daily Revenue: {}".format(average_daily_revenue))

# Find the haircuts that cost less than $30
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]
print(cuts_under_30)