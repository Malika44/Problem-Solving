Hi there 
•Problem of the day:

Birthday Cake Candles.

Count how many Candles are the tallest

candles = [4,1,4,3]

→The tallest candles are 4 unit high there are 2 candles with this hight" 

return th number of Candles that are tallest.
Code:
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


