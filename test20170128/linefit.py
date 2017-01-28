import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import datetime
import sys
print datetime.datetime.now()
#x = np.linspace(0,1,50)
#y = np.cos(x)+0.1*np.random.rand(50)
inputpath = "D:/demo/"
outputpath = "D:/demo/"
infn1 = "midrun2.csv"

df = pd.read_csv(inputpath +infn1, sep=',',low_memory=False)
t0 = df["time"].min()
tm = df["time"].max()
dl = len(df)
#plt.axis([0,2000, -50, 200])
x = df["midrun-tps"][0:dl]#(0,9594,18234)
y = df["cpu_used_pct"][0:dl]
plt.figure(4)
cof = np.polyfit(x,y,1)
p = np.poly1d(cof)
r = np.corrcoef(x,y)
r2 = (r*r)[0,1]
print "k=",cof[0]
print "b=",cof[1]
print "r2=",r2
print p
plt.plot(x,y,'o',x,p(x),lw=2)
plt.title('plot-'+infn1+'(2016-12-09~14)')
plt.legend(["R2=%r" % round(r2,4),p], loc="upper left") #"k=%r" %round(cof[0],5),"b=%r" % cof[1]
plt.grid(4)
plt.savefig('d:/midrun2.pdf',dpi = 200)
plt.show(4)
step = 10  #10min
win =  60*24*2

plt.ion()
for i in range(1,int(dl/step)):
    if i <= win/step:
        x = df["midrun-tps"][0:(step*i)]
        y = df["cpu_used_pct"][0:(step*i)]
    else:
        x= df["midrun-tps"][(i*step-win):(step*i)]
        y = df["cpu_used_pct"][(i*step-win):(step*i)]
    #t = df["time"][(10*i)]
    cof = np.polyfit(x,y,1)
    p = np.poly1d(cof)
    r = np.corrcoef(x,y)
    r2 = (r*r)[0,1]
    k = cof[0]
    b = cof[1]
    tps = (70 - b)/k
    plt.figure(1)
    plt.axis([0,int(round(dl/step,-2)), -50, 300])
    plt.title(infn1+'max tps=(70-b)/k')
    plt.scatter(i, tps,c="m",label='tps',s = 20,alpha=1)
    plt.grid(1)
    plt.savefig('d:/plot-max-tps.pdf',dpi = 200)
    plt.figure(2)
    plt.axis([0,int(round(dl/step,-2)), -1, 1])
    plt.title(infn1+'slope k=green,r2=red')
    plt.scatter(i, r2,c="r",label='r2',s = 20,alpha=1)
    plt.scatter(i, k,c="g",label='k',s = 20,alpha=1)
    plt.grid(2)
    plt.savefig('d:/plot-k&r2.pdf',dpi = 200)
    plt.figure(3)
    plt.axis([0,int(round(dl/step,-2)), -5, 10])
    plt.title(infn1+'intercept b=blue')
    plt.scatter(i, b,c="b",label='b',s = 20,alpha=1)
    plt.grid(3)
    plt.savefig('d:/plot-b.pdf',dpi = 200)
    plt.pause(0.01)


#plt.plot(x,y,'o',x,p(x),lw=2)
#plt.show()


