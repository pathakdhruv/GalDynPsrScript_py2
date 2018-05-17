from __future__ import print_function
import math
import numpy as np
import parameters as par
from ExcessZ import g
from Excesspl import aplmod
from Excesspl import Rpkpcfunc
from Excesspl import Vprat
from err_NT import errNT
from err_excesspl_Reid import err_Reid14




def calc(bdeg, sigb, ldeg, sigl, dkpc, sigd, Har):           
      b = bdeg*par.degtorad
      l = ldeg*par.degtorad
      zkpc = dkpc*math.sin(b)

      adrc = aplmod(dkpc,b,l)*math.cos(b) #s^-1
      errReid = err_Reid14(bdeg, sigb, ldeg, sigl, dkpc, sigd) #s^-1
      azbcnt = g(zkpc)*math.sin(b) #s^-1
      errnt = errNT(bdeg, sigb, dkpc, sigd) #s^-1


      if Har==1:
         print ("Excess_parallel_Reid2014, Excess_z_NT95 = ", adrc,", ", azbcnt)

      else:      
         print ("Excess_parallel_Reid2014, Excess_z_NT95 = ", adrc,"+/-",errReid, ", ", azbcnt,"+/-",errnt)
         

      return None;
