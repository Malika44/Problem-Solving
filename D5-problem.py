# Read height from user
n = int(input("Enter height: "))

# Estimate the max width for the bottom row
# Example: for n = 4 -> bottom row: 1 2 4 8 4 2 1
# So total numbers = 2n - 1, each number + space
max_row = []
for j in range(n):
    max_row.append(str(2 ** j))
for j in range(n - 2, -1, -1):
    max_row.append(str(2 ** j))
max_width = len(' '.join(max_row))

# Generate rows
for i in range(1, n + 1):
    row = []

    # Left side: 2^0 to 2^(i-1)
    for j in range(i):
        row.append(str(2 ** j))

    # Right side: 2^(i-2) down to 2^0
    for j in range(i - 2, -1, -1):
        row.append(str(2 ** j))

    # Join and center
    line = ' '.join(row).center(max_width)
    print(line)
