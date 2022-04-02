import random

x = []
y = []
for i in range(0, 1000):
    x.append(random.randint(0, 30))
    y.append(random.randint(0, 1))

f=open("train.csv",'w')
for i in range(len(x)):
    f.write("{},{}\n".format(x[i], y[i]))

f.close()
