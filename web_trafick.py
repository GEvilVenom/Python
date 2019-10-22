import scipy as sp
import matplotlib.pyplot as plt
data = sp.genfromtxt("web_trafick.tsv", delimiter="\t")
print(data[:10])
print(data.shape)
x=data[:,0]
y=data[:,1]
x=x[~sp.isnan(y)]
y=y[~sp.isnan(y)]
plt.scatter(x,y)
plt.title("Web Traffic")
plt.xlabel("TIme")
plt.ylabel("Hits/Hr")
plt.autoscale(tight=True)
#autoscale to automatically scale the figure in console window
plt.grid()
plt.show()