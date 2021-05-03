# -*- coding: utf-8 -*-
"""
fait le Mon Apr 12 10:47:29 2021

par thibault pelliccia
how da fuk does that thing work
"""
import math as m
import numpy as np
import matplotlib.pyplot as pp



def g(f,fp,x):
    return x-f(x)/fp(x)
#############################################

def f1(x):
    return x**4 + 3*x - 9
def f1p(x):
    return 4*(x**3)+3
def g12(x):
    return (9-3*x)**(1/4)
#############################
def f4(x):
    return m.exp(x)-x-10
def f4p(x):
    return m.exp(x)-1
def g41(x):
    return m.log(x + 10)
def g42(x):
    return m.exp(x) - 10
#############################
def f6(x):
    return m.exp(x)-(x**2)-3
def f6p(x):
    return m.exp(x)-2*x
def g61(x):
    return m.log((x**2)+3)
def g62(x):
    return m.sqrt(m.exp(x)-3)
#############################
def g101(x):
    return m.log(10/m.log((x**2)+4))
def g102(x):
    return m.sqrt(m.exp(10/m.exp(x))-4)
def f10(x):
    return m.log(x**2+4)*m.exp(x)-10
def f10p(x):
    return ((2*x))/((x**2)+4)*m.exp(x)+m.log(x**2+4)*m.exp(x)

#############################################
def G(x):
    return (1+m.sin(x))/2
def F(x):
    return 2*x-(1+m.sin(x))
def Fp(x):
    return 2-m.cos(x)


def dicho(f,a,b,epsilon,nitermax):
    m=0
    n=1
    L=[[],[],[]]
    L[1].append(m)
    L[2].append(abs(a-b))
    L[0].append(n)
    while(b-a)>epsilon or n<=nitermax:
        m=(a+b)/2
        if (f(a)*f(m)<=0):
            b=m
        else:
            a=m
        n+=1
        erreur=a-b
        #print(m,erreur,n)
        L[1].append(m)
        L[2].append(abs(erreur))
        L[0].append(n)
    return L


def sec(f,x0,x1,epsilon,nitermax):
    a=x0
    b=x1
    n=0
    L=[[],[],[]]
    c = b-f(b)*(a-b)/(f(a)-f(b))  
    L[1].append(c)
    L[2].append(abs(a-c))
    L[0].append(n)
    
    while abs(a-c)>epsilon or n<=nitermax:
        n+=1
        a, c = c, c-f(c)*(c-a)/(f(c)-f(a))
        erreur=(a-c)
        #print(c,erreur,n)
        L[1].append(c)
        L[2].append(abs(erreur))
        L[0].append(n)
    return L
        
def newton(f,fp,x0,epsilon,Nitermax) :
    n=0
    xold=x0
    xnew=g(f,fp,xold)
    erreur=(xnew-xold)
    L=[[],[],[]]
    L[1].append(xnew)
    L[2].append(abs(erreur))
    L[0].append(n)
    while ( abs(erreur) > epsilon) and n<Nitermax:
        xnew=g(f,fp,xold)
        erreur=xnew-xold
        xold=xnew
        print(xnew,erreur,n)
        L[1].append(xnew)
        L[2].append(abs(erreur))
        L[0].append(n)
        n+=1
    return L

def point_fixe(g,x0,epsilon,Nitermax) :
    n=0
    xold=x0
    xnew=g(xold)
    erreur=(xnew-xold)
    L=[[],[],[]]
    L[0].append(n) 
    L[1].append(xnew)
    L[2].append(abs(erreur))
    while ( abs(erreur) > epsilon) and n<Nitermax:
        xnew=g(xold)
        erreur=xnew-xold
        xold=xnew
        
        #print(xnew,erreur,n)
        n+=1
        L[0].append(n) 
        L[1].append(xnew)
        L[2].append(abs(erreur))
    return L   

def graph(lp,ln,ld,ls):
    pp.grid(True, which="both")
    #pp.plot(lp[0],lp[2])
    #pp.plot(ln[0],ln[2],plotfuncs=‘semilogy’)
    #pp.plot(ld[0],ld[2])
    #pp.plot(ls[0],ls[2])
    pp.semilogy(lp[0], lp[2],'m') #point fixe : magenta
    pp.semilogy(ln[0], ln[2],'g') #newton : vert
    pp.semilogy(ld[0], ld[2],'r') #dichotomie : rouge
    pp.semilogy(ls[0], ls[2],'b') #sécante : bleu
    pp.show()


def main():

    lp=[[]]
    ln=[[]]
    ld=[[]]
    ls=[[]]
    lp=point_fixe(g101,1, 1e-10, 1e4)
    ln=newton(f10,f10p,1, 1e-10, 1e4)
    ld=dicho(f10,0,1,1e-10,1e-4)
    ls=sec(f10,1,4,1e-10,1e-4)
    print("lp=",lp,sep='\n')
    print("ln=",ln,sep='\n')
    print("ld=",ld,sep='\n')
    print("ls=",ls,sep='\n')
    graph(lp,ln,ld,ls)
    
main()