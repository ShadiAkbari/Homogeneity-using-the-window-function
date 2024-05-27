import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

vorud=pd.read_csv(r"C:\Users\USER\Desktop\t\galaxies.csv")
X=np.array(vorud["x [Mpc]"].tolist())
Y=np.array(vorud["y [Mpc]"].tolist())

plt.scatter(X,Y,s=0.1)
plt.show()


ST = []
L = []
for num in [1,2,5,10,20,50,100]:
    X1 = np.floor(X / num)
    Y1 = np.floor(Y / num)
    N = np.zeros((1000//num,1000//num))
    for k in range(len(X1)):
        N[int(X1[k]+len(N)/2)][int(Y1[k]+len(N)/2)]+=1
    mu = np.average(N/num**2)
    sig = np.std(N/num**2)
    ST.append(sig)
    L.append(num)
plt.plot(L,ST,scalex = 'log')
plt.show()

plt.imshow(N/num**2, cmap='gray')
plt.show()
