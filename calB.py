from __future__ import print_function
import math
import numpy as np
import parameters as par
from ExcessZ import fhigh
from ExcessZ import flow
from Excesspl import aplold
from Excesspl import Rpkpcfunc
from err_HFhigh import errHFhi
from err_HFlow import errHFlo
from err_excesspl_Damour import err_DT91


def calb(bdeg, sigb, ldeg, sigl, dkpc, sigd, Har):
      global excpl,exz           
      b = bdeg*par.degtorad
      l = ldeg*par.degtorad
      zkpc = dkpc*math.sin(b)
      if zkpc<0.0:
         zkpcm = -zkpc
      else:
         zkpcm = zkpc
      adrcold = aplold(dkpc,b,l)*math.cos(b) #s^-1
      errDT91 = err_DT91(bdeg, sigb, ldeg, sigl, dkpc, sigd) #s^-1

      azbchfh = fhigh(zkpc)*math.sin(b)*1.08100761142e-19 #s^-1
      azbchfl = flow(zkpc)*math.sin(b)*1.08100761142e-19 #s^-1
      errhi = errHFhi(bdeg, sigb, dkpc, sigd) #s^-1
      errlo = errHFlo(bdeg, sigb, dkpc, sigd) #s^-1


      if Har==1:
         if zkpcm<=1.5:
            print ("Excess_parallel_DT91, Excess_z_HF04fit = ", adrcold,", ", azbchfl)
            excpl = adrcold
            exz = azbchfl
         else:
            print ("Excess_parallel_DT91, Excess_z_HF04fit = ", adrcold,", ", azbchfh)
            excpl = adrcold
            exz = azbchfh 
      else:      
         if zkpcm<=1.5:
            print ("Excess_parallel_DT91, Excess_z_HF04fit = ", adrcold,"+/-",errDT91, ", ", azbchfl,"+/-",errlo)
            excpl = adrcold
            exz = azbchfl
         else:
            print ("Excess_parallel_DT91, Excess_z_HF04fit = ", adrcold,"+/-",errDT91, ", ", azbchfh,"+/-",errhi)
            excpl = adrcold
            exz = azbchfh
         
      return None;

def Explb():
   return excpl;

def Exzb():
   return exz;
