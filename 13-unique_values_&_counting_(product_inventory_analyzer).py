import numpy as np

product_ids = np.array([101, 102, 101, 103, 102, 101, 104, 103])
available_products = np.array([101, 103, 104])
print("Products IDs: \n",product_ids)

print("\n1. Find unique product IDs:")
# np.unique(): Returns the unique values in an array without duplicates.
unique_products=np.unique(product_ids)
print(unique_products)

print("\n2. Count the occurrences of each product ID:")
# np.unique(..., return_counts=True):
# Returns the unique values and the number of occurrences of each value.
unique_ids,counts=np.unique(product_ids,return_counts=True)
print("Product ID | Occurrences")
print("------------------------")
# Note: zip() combines corresponding elements from multiple iterables into pairs or tuples.
# It is commonly used with a for loop to process related values together. 
# If the iterables have different lengths, zip() stops at the shortest one.
for product_id, count in zip(unique_ids, counts):
    print(f"{product_id:^10} | {count:^11}")

print("\n3. Check which products are available in the inventory:")
# np.isin(): Checks whether each element of an array exists in another array.
product_availability= np.isin(product_ids,available_products)
for product_id, is_available in zip(product_ids, product_availability):
    print(f"{product_id:^10} | {str(is_available):^9}")

print("\n4. Extract the IDs of available products:")
available_products_ids=product_ids[product_availability]
print(np.unique(available_products_ids))
