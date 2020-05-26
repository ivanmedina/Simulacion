import random
import math
def uniforme(a,b):
     x=0.0
     y=0.0
     y=random.random()/32767.0
     x=y*(b-a)+a
     return(x)

def exponencial(m):
    x=0.0
    y=0.0
    x=-1*m*math.log(1-y)
    return(x)


def erlang(k,m):
    x=0.0
    me=0.0
    me=m/k
    for i in range(1,k):
        x=x+exponencial(me)
    return(x)

def normal(m,v):
    x=0.0
    z=0.0
    sum=0.0
    for i in range(1,12):
        sum =sum+ uniforme(0,1)
    z=sum-6
    x=math.sqrt(v)*z+m
    return x

def geometrica(p):
    x=1
    f=p
    s=f
    y=uniforme(0,1)
    while(y<s):
        f=f*(1-p)
        s=s+f
        x=x+1
    return

def poisson(lam):
    x=1
    f=math.exp(-1*lam)
    s=f
    y=uniforme(0,1)
    while(y>s):
        f=f*lam/(x+1)
        s=s+f
        x=x+1
    return x

def binomial(n,p):
    x=0
    f=math.exp(n*math.log(1-p))
    s=f
    y=uniforme(0,1)
    while(y>s):
        f=f*p*(n-x)/((x+1)*(1-p))
        s=s+1
        x=x+1
    return x

def aleatoria(tipo, par1, par2):
    x=0.0
    options={
        0: poisson(par1),
        1: erlang(par1,par2),
        2: normal(par1,par2),
        3: binomial(par1,par2),
        4: uniforme(par1,par2),
        5: geometrica(par1)
    }
    x=options.get(tipo,lambda:"Invalid Month")
    return x
