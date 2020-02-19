# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 15:46:06 2020

@author: posch
"""


import random as rd
import numpy as np
import matplotlib.pyplot as plt
def huge_plot_2(E=70000,SIG_Y=300 ,v=0.3,eta_min=-0.005,eta_max=0.005,NC=500):
    eta_min=float(eta_min)
    eta_max=float(eta_max)
    G=float(E)/(2.*(1+v))
    
    SIG_R_1=np.zeros(NC)
    SIG_G_1=np.zeros(NC)
    SIG_R_2=np.zeros(NC)
    SIG_G_2=np.zeros(NC)
    for i in range(1,NC):
       EPS_XX=rd.uniform(eta_min,eta_max)
       EPS_YY=rd.uniform(eta_min,eta_max)
       GAM_XY=rd.uniform(eta_min,eta_max)
       SIG_XX=(E/(1-v**2))*(EPS_XX+v*EPS_YY)
       SIG_YY=(E/(1-v**2))*(EPS_YY+v*EPS_XX)
       TAU_XY=G*GAM_XY    
       SIG_1=((SIG_XX+SIG_YY)/2)+np.sqrt(((SIG_XX-SIG_YY)/2)**2+TAU_XY**2)
       SIG_2=((SIG_XX+SIG_YY)/2)-np.sqrt(((SIG_XX-SIG_YY)/2)**2+TAU_XY**2)
       SIG_v3=np.sqrt(0.5*((SIG_1-SIG_2)**2+SIG_1**2+SIG_2**2))
       f=SIG_v3-SIG_Y   
       if f<0:
           SIG_G_1[i]=SIG_1
           SIG_G_2[i]=SIG_2
       elif f>0: 
           SIG_R_1[i]=SIG_1
           SIG_R_2[i]=SIG_2       
    plt.plot(SIG_G_1,SIG_G_2,'go')
    plt.plot(SIG_R_1,SIG_R_2,'ro')  
    plt.plot(-SIG_G_1,-SIG_G_2,'go')
    plt.plot(-SIG_R_1,-SIG_R_2,'ro')     