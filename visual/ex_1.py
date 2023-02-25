import matplotlib.pyplot as plt
x1 = [1,2,3,4,5,6]
y1 = [2,4,6,18,12,12]

x2 = [2,6,8]
y2 = [6,4,9]

plt.plot(x2,y2,linestyle=":")
plt.plot(x1,y1)
plt.title("test",fontsize=20, color="red")
plt.xlabel("x-axis")





plt.show()