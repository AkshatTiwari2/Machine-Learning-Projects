import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
x = pd.read_csv(r"Linear_X_Train.csv").values
y = pd.read_csv(r"Linear_Y_Train.csv").values

theta = np.load("ThetaList.npy")

plt.ion()

T0 = theta[:,0]
T1 = theta[:,1]

for i in range(0,50,3):
    y_ = T1[i]*x +T0
    plt.scatter(x,y)
    plt.plot(x,y_,'red')
    plt.draw()
    plt.pause(1)
    plt.clf()
