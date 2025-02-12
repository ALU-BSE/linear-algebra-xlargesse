# import pandas as pd
# import numpy as np

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

    # Iterate over the elements of the current row 
    # (Prices[i]) and multiply each element by its 
    # corresponding element in Array2.
    for j in range(len(Prices[0])):
        # Find the product of Prices[i][j] and 
        # Array2[j] and add it to the sum.
        row_sum += Prices[i][j] * Array2[j]
        # If we have reached the end of the row, append the sum to the Ans list.
        if j == len(Prices[0]) - 1:
            Ans.append(row_sum)
        else:
            continue
print(f"Result: {Ans}")