import scipy as sp
import matplotlib.pyplot as plt

data = sp.genfromtxt("web_trafick.tsv", delimiter = '\t')
x= data[:,0]
y=data[:,1]
x= x[~sp.isnan(y)]
y=y[~sp.isnan(y)]
plt.scatter(x,y)
plt.show()


fpq_one,residuals_one,rank_one,su_one,rcond_one = sp.polyfit(x,y,1,full = True)
fpq_two,residuals_two,rank_two,su_two,rcond_two = sp.polyfit(x,y,2,full = True)
fpq_three,residuals_three,rank_three,su_three,rcond_three = sp.polyfit(x,y,3,full = True)
fpq_ten,residuals_ten,rank_ten,su_ten,rcond_ten = sp.polyfit(x,y,10,full = True)

f1 = sp.poly1d(fpq_one)
f2 = sp.poly1d(fpq_two)
f3 = sp.poly1d(fpq_three)
f4 = sp.poly1d(fpq_ten)

def error(f,x,y):
    return sp.sum((y-f(x))**2)
               
fx = sp.linspace(0, x[-1], 1000)

plt.scatter(x,y)
plt.plot(fx,f1(fx),linewidth = 4,color='red',label="Order 1")
plt.plot(fx,f2(fx),linewidth = 4,color='green',label="Order 2")
plt.plot(fx,f3(fx),linewidth = 4,color='cyan',label="Order 3")
plt.plot(fx,f4(fx),linewidth = 4,color='magenta',label="Order 10")
plt.legend()
plt.show()
err1 = error(f1,x,y)
err2 = error(f2,x,y)
err3 = error(f3,x,y)
err4 = error(f4,x,y)
print("The errors are")
errors = {"Order 1":err1, "Order 2": err2, "Order 3": err3, "Order 10": err4}

print('Name Age')
for o, r in errors.items():
    print('{} {}'.format(o, r))
