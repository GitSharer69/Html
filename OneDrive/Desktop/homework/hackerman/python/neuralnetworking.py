import numpy as np
input_vector = [1.72, 1.23]
weights_1 = [1.26, 0]
weights_2 = [2.17, 0.32]
# first_indexes_mult = input_vector[0] * weights_1[0]
# second_indexes_mult = input_vector[1] * weights_1[1]
# dot_product_1 = first_indexes_mult + second_indexes_mult

# Out[8]: The dot product is: 2.1672
dot_product_2 = np.dot(input_vector, weights_2)
dot_product_1 = np.dot(input_vector, weights_1)
print(f"The dot product is: {dot_product_2}")