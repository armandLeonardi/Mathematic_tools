# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 12:56:17 2019

@author: Marsupilami
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

mu1  = 0
sig1 = 1

mu2 = 3
sig2 = 0.1

mu3 = -2
sig3 = 3

MU = [mu1,mu2,mu3]
SIG = [sig1,sig2,sig3]

def nPdf(x,m,s):
    return stats.norm.pdf(x,m,s)

def functional_nPdf(f,x,params):
    return nPdf(f(x,**params),0,1)

xnew = np.random.normal(mu2,sig2,8)

L = [np.prod(nPdf(xnew,m,s)) for m,s in zip(MU,SIG)]

X = np.linspace(-4,4,100)
for m,s in zip(MU,SIG):
    plt.plot(X,nPdf(X,m,s))



#%%

class Mlh:
    
    def __init__(self,verbose = False):
        self.version = '1.0'
        self.mu = 0
        self.sigma = 1
        self.verbose = verbose
        
    def nPdf(self,x,m,s):
        return stats.norm.pdf(x,m,s)

    def functional_nPdf(self,f,x,param):
        return nPdf(f(x,**param),self.mu,self.sigma)

    def _compute_L(self,X,mu,sig):
        return np.prod(self.nPdf(X,mu,sig))
    
    def _compute_f_L(self,f,X,param):
        return np.prod(self.functional_nPdf(f,X,param))
    
    def search(self,X,params):
        L = sorted([self._compute_L(X,m,s) for m,s in params],reverse=True)
        self.pprint(self.verbose,"Search ended three first result on %s :\n%s"%(len(L),list(zip(params[:3],L[:3]))))
        return L

    def search_f(self,f,X,params):
        L = [self._compute_f_L(f,X,param) for param in params]
        self.pprint(self.verbose,"Search ended with f : %s\nparams %s\nThree first result on %s \n %s"%(f,params[:3],len(L),L[:3]))
        return 0

    def pprint(self,verbose,string):
        if verbose:
            print(string)
            
            
mlh = Mlh(True)
mlh.search(xnew,list(zip(MU,SIG)))


