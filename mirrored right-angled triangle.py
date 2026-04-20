# Set the number of rows
rows = 5

# Iterate through each row
for i in range(1, rows + 1):
    # Print (rows - i) spaces followed by (i) stars
    print(" " * (rows - i) + "*" * i)
