from __future__ import print_function
import math
import numpy as np
import parameters as par
from ExcessZ import fhigh
from ExcessZ import flow
from Excesspl import Rpkpcfunc
from err_HFhigh import errHFhi
from err_HFlow import errHFlo
from galpyMWpl import MWpl

def calia(bdeg, sigb, ldeg, sigl, dkpc, sigd, Har):
      global excpl,exz           
      b = bdeg*par.degtorad
      l = ldeg*par.degtorad
      zkpc = dkpc*math.sin(b)
      if zkpc<0.0:
         zkpcm = -zkpc
      else:
         zkpcm = zkpc


      azbchfh = fhigh(zkpc)*math.sin(b)*1.08100761142e-19 #s^-1
      azbchfl = flow(zkpc)*math.sin(b)*1.08100761142e-19 #s^-1
      errhi = errHFhi(bdeg, sigb, dkpc, sigd) #s^-1
      errlo = errHFlo(bdeg, sigb, dkpc, sigd) #s^-1

      Excpl = MWpl(bdeg,ldeg,dkpc) #s^-1    


      if zkpcm<=1.5:
         print ("Excess_parallel_galpy(from Vp/Vs, without BH), Excess_z_HF04fit = ", Excpl,", ", azbchfl)
         excpl = Excpl
         exz = azbchfl
      else:
         print ("Excess_parallel_galpy(from Vp/Vs, without BH), Excess_z_HF04fit = ", Excpl,", ", azbchfh)
         excpl = Excpl
         exz = azbchfh
        
      return None;


def Explia():
   return excpl;

def Exzia():
   return exz;
