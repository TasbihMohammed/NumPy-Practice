import numpy as np

prices = np.array([100, 250, 80, 400, 150])
print(prices)

print("Increase all prices by 10%.")
increased_prices=prices*1.10
print(increased_prices)

print("Subtract 20 from each price.")
reduced_prices=prices-20
print(reduced_prices)

print("Calculate the sum of all prices.")
print(prices.sum())

print("Calculate the average price.")
print(prices.mean())

print("Find the maximum and minimum prices.")
print("Max:")
print(prices.max())
print("Min:")
print(prices.min())
