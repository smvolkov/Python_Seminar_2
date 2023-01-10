pupils = [165, 163, 160, 160, 157, 157, 155, 154]
petya = 162

for i in range(1, len(pupils)+1):
    if (petya <= pupils[i-1]) and (petya > pupils[i]):
        print(i+1)
        break
