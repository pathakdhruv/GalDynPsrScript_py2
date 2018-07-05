from __future__ import print_function
import math
import numpy as np
import parameters as par
from err_Shklovskii import err_Shkl



def shk(dkpc, sigd):
  global mu_T,mu_alpha, sigmua, mu_delta, sigmud, Pshks, errshkl  
  c= par.c

  mu_alphar, sigmuar = raw_input("Enter the proper motion of the pulsar in right ascension (mas yr^-1), error in mu_alpha(sigmua) [separated by comma]: ").split((','))
  mu_deltar, sigmudr = raw_input("Enter the proper motion of the pulsar in declination (mas yr^-1), error in mu_delta(sigmud) [separated by comma]: ").split((','))

  mu_alpha = float(mu_alphar)
  sigmua = float(sigmuar)
  mu_delta = float(mu_deltar)
  sigmud = float(sigmudr)    

  mu_T = pow((mu_alpha*mu_alpha + mu_delta*mu_delta),0.5) # mas/yr
  Pshk = (dkpc*(mu_T*mu_T))/c #kpc*(mass yr-1)/(m/s)
  Pshks = (2.42924681374e-21)*dkpc*(mu_T*mu_T) #s^-1
  errshkl = err_Shkl(dkpc, sigd, mu_alpha, sigmua, mu_delta, sigmud)
   
  print ("The Shlovskii term contribution is: ", Pshks,"+/-",errshkl)

  return None;

def Exshk():
   return Pshks;

def errShk():
   return errshkl;
