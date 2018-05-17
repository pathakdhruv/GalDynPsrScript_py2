from __future__ import print_function
import math
import numpy as np
import parameters as par
from ExcessZ import g
from Excesspl import aplold
from Excesspl import Rpkpcfunc
from err_NT import errNT
from err_excesspl_Damour import err_DT91


def cala(bdeg, sigb, ldeg, sigl, dkpc, sigd, Har):           
      b = bdeg*par.degtorad
      l = ldeg*par.degtorad
      zkpc = dkpc*math.sin(b)

      adrcold = aplold(dkpc,b,l)*math.cos(b) #s^-1
      errDT91 = err_DT91(bdeg, sigb, ldeg, sigl, dkpc, sigd) #s^-1
      azbcnt = g(zkpc)*math.sin(b) #s^-1
      errnt = errNT(bdeg, sigb, dkpc, sigd) #s^-1



      if Har==1:
         print ("Excess_parallel_DT91, Excess_z_NT95 = ", adrcold,", ", azbcnt)
      else:
         print ("Excess_parallel_DT91, Excess_z_NT95 = ", adrcold,"+/-",errDT91, ", ", azbcnt,"+/-",errnt)

     

      return None;
