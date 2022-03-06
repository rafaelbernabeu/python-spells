import matplotlib.pyplot as plt

x = 696967
result = []

while True:

    if (x % 2) == 0:
        x = int(x / 2)
    else:
        x = int(3 * x + 1)

    print(x)
    result.append(x)
    
    if x == 1 :
        break


plt.plot(result)
plt.show()