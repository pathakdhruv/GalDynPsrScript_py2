from __future__ import print_function
import math
import numpy as np
import parameters as par
from ExcessZ import fhigh
from ExcessZ import flow
from Excesspl import aplmod
from Excesspl import Rpkpcfunc
from Excesspl import Vprat
from err_HFhigh import errHFhi
from err_HFlow import errHFlo
from err_excesspl_Reid import err_Reid14


def cald(bdeg, sigb, ldeg, sigl, dkpc, sigd, Har): 
      global excpl,exz, errpl, errz           
      b = bdeg*par.degtorad
      l = ldeg*par.degtorad
      zkpc = dkpc*math.sin(b)
      if zkpc<0.0:
         zkpcm = -zkpc
      else:
         zkpcm = zkpc
      adrc = aplmod(dkpc,b,l)*math.cos(b) #s^-1
      errReid = err_Reid14(bdeg, sigb, ldeg, sigl, dkpc, sigd) #s^-1

      azbchfh = fhigh(zkpc)*math.sin(b)*1.08100761142e-19 #s^-1
      azbchfl = flow(zkpc)*math.sin(b)*1.08100761142e-19 #s^-1
      errhi = errHFhi(bdeg, sigb, dkpc, sigd) #s^-1
      errlo = errHFlo(bdeg, sigb, dkpc, sigd) #s^-1


      if Har==1:
         if zkpcm<=1.5:
            print ("Excess_parallel_Reid2014, Excess_z_HF04fit = ", adrc,", ", azbchfl)
            print ("Vp/Vs= ", Vprat(Rpkpcfunc(dkpc,b,l,par.Rskpc)))
            excpl = adrc
            exz = azbchfl
         else:
            print ("Excess_parallel_Reid2014, Excess_z_HF04fit = ", adrc,", ", azbchfh)
            print ("Vp/Vs= ", Vprat(Rpkpcfunc(dkpc,b,l,par.Rskpc)))
            excpl = adrc
            exz = azbchfh      
      else:
    
         if zkpcm<=1.5:
            print ("Excess_parallel_Reid2014, Excess_z_HF04fit = ", adrc,"+/-",errReid, ", ", azbchfl,"+/-",errlo)
            print ("Vp/Vs= ", Vprat(Rpkpcfunc(dkpc,b,l,par.Rskpc)))
            excpl = adrc
            exz = azbchfl 
            errpl = errReid 
            errz = errlo   
         else:
            print ("Excess_parallel_Reid2014, Excess_z_HF04fit = ", adrc,"+/-",errReid, ", ", azbchfh,"+/-",errhi)
            print ("Vp/Vs= ", Vprat(Rpkpcfunc(dkpc,b,l,par.Rskpc)))
            excpl = adrc
            exz = azbchfh
            errpl = errReid 
            errz = errhi
      return None;


def Expld():
   return excpl;

def Exzd():
   return exz;

def Errpld():
   return errpl;

def Errzd():
   return errz;
