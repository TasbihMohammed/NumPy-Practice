# Broadcasting in NumPy:
# Broadcasting allows NumPy to perform element-wise operations on arrays
# with different shapes without manually repeating data.
# NumPy compares their dimensions to determine whether the operation is valid.

import numpy as np

prices = np.array([100, 200, 300, 400])
tax_rate = np.array([0.14])
print("Prices: \n",prices)
print("Tax rate: ",tax_rate)

print("Add the tax rate to each product price: ")
prices_after_tax = prices * (1 + tax_rate)
print(prices_after_tax)

print("Apply different discounts to the products using this array:")
discount_percentages = np.array([10, 20, 30, 40])
print(discount_percentages)
print("note: Each discount is a percentage of the corresponding product price.")
prices_after_discount=prices*((100-discount_percentages)/100)
print(prices_after_discount)

print("Create a 2D array representing prices for three stores: ")
store_prices = np.array([
    [100, 200, 300, 400],
    [110, 190, 310, 420],
    [95, 210, 290, 380]
])
print("Add a different delivery fee to each product across all three stores:")
delivery_fees = np.array([5, 10, 15, 20])
prices_with_delivery = store_prices + delivery_fees
print(prices_with_delivery)

print("Apply a different discount percentage to each store:")
store_discounts = np.array([[0.10], [0.05], [0.15]])
prices_with_discount=prices_with_delivery*(1-store_discounts)
print(prices_with_discount)

