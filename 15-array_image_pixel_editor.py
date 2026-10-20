import numpy as np

# Create a 2D array representing a grayscale image.
# Pixel values range from 0 (black) to 255 (white).
image = np.array([
    [0, 50, 100, 150, 200],
    [25, 75, 125, 175, 225],
    [50, 100, 150, 200, 250],
    [75, 125, 175, 225, 255],
    [100, 150, 200, 250, 255]
])

print("1. Original Image:")
print(image)
print("Image Shape:", image.shape)


# Use np.where() to increase pixel values below 100 by 50.
# Keep all other pixel values unchanged.
brightened_image = np.where(image < 100, image + 50, image)

print("\n2. Brightened Image:")
print(brightened_image)


# Use np.zeros_like() to create a zero-filled array
# with the same shape and data type as the original image.
mask = np.zeros_like(image)

# Set mask positions to 1 wherever the original pixel is below 100.
mask[image < 100] = 1

print("\n3. Dark-Pixel Mask:")
print(mask)


# Use np.ones_like() to create an array of ones
# with the same shape and data type as the original image.
white_image = np.ones_like(image)

# Replace all ones with 255 to create a completely white image.
white_image[white_image == 1] = 255

print("\n4. White Image:")
print(white_image)


# Use np.copy() to create an independent copy of the original image.
image_copy = np.copy(image)

# Modify one pixel in the copy without changing the original image.
image_copy[0, 0] = 144

print("\n5. Original Image After Copy Modification:")
print(image)

print("\nModified Copy:")
print(image_copy)


# Use np.array_equal() to check whether two arrays
# have the same shape and identical values.
print("\nAre the Original Image and Modified Copy Identical?")
print(np.array_equal(image, image_copy))


