import matplotlib.pyplot as plt

figure, ax = plt.subplots()

x = [1,2,3,4,5]
y = [1,4,9,16,25]

ax.plot(x,y)

figure.savefig('test.jpg')
