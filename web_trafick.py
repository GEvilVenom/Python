import scipy as sp
import matplotlib.pyplot as plt
data = sp.genfromtxt("web_trafick.tsv", delimiter="\t")
print(data[:10])
print(data.shape)
x=data[:,0]
y=data[:,1]
x=x[~sp.isnan(y)]
y=y[~sp.isnan(y)]


#fp1,residuals,rank,su,rcond=sp.polyfit(x,y,1,full=True) {AFTER DEF ERROR()}
fp1=sp.polyfit(x,y,1,full=True)
f1=sp.poly1d(fp1)
def error(f,x,y):
     return sp.sum((y-f(x))**2)
    
print(error(f1,x,y))
fx=sp.linspace(0,x[-1],1000)



plt.scatter(x,y)
plt.title("Web Traffic")
plt.xlabel("TIme")
plt.ylabel("Hits/Hr")
plt.autoscale(tight=True)
plt.plot(fx,f1(fx),linewidth=4)
#autoscale to automatically scale the figure in console window
plt.grid()
plt.show()
