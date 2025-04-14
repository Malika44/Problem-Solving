Hi there 
candles = [4, 1, 4, 3]
tallest = candles[0]  

for height in candles:
    if height > tallest:
        tallest = height  

count = 0
for height in candles:
    if height == tallest:
        count += 1

print(count)


