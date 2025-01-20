import pandas as pd
import numpy as np

# Load data
#data = pd.read_csv('path/to/data')

# Example arrays
Prices = [[300, 500],
          [1000, 120.85]]

Array2 = [200, 100]

# Calculate the result
Ans = []
# (300*200 + 500*100) as an example calculation

#Traverse through each row in Prices.
for i in range(len(Prices)):
    # Initialize the sum for the current row.
    row_sum = 0
    for j in range(len(Prices[0])):
        # Find the product of Prices[i][j] and Array2[j] and add it to the sum.
        row_sum += Prices[i][j] * Array2[j]