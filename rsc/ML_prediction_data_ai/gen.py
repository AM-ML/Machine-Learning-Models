import numpy as np
from pandas import DataFrame

# Set a random seed for reproducibility
np.random.seed(42)

# Number of data points
num_samples = 100000

# Generate random values for 'a', 'b', and 'c'
a_values = np.random.randint(0, 100, num_samples)
b_values = np.random.randint(0, 100, num_samples)
c_values = np.random.randint(0, 100, num_samples)

# Simulate a relationship between 'a', 'b', 'c' and 'outcome'
outcome_values = a_values + b_values - c_values

# Create a DataFrame
data = DataFrame({'a': a_values, 'b': b_values, 'c': c_values, 'outcome': outcome_values})

# Save the synthetic data to a CSV file
data.to_csv('data3.csv', index=False)
