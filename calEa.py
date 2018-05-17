from __future__ import print_function
import math
import numpy as np
import parameters as par
from Excesspl import aplold
from Excesspl import Rpkpcfunc
from err_excesspl_Damour import err_DT91
from galpyMWZfo import MWZfo

def calea(bdeg, sigb, ldeg, sigl, dkpc, sigd, Har):           
      b = bdeg*par.degtorad
      l = ldeg*par.degtorad
      zkpc = dkpc*math.sin(b)

      adrcold = aplold(dkpc,b,l)*math.cos(b) #s^-1
      errDT91 = err_DT91(bdeg, sigb, ldeg, sigl, dkpc, sigd) #s^-1
      Excz = MWZfo(bdeg,ldeg,dkpc)



      print ("Excess_parallel_DT91, Excess_z_galpy(without BH) = ", adrcold,", ", Excz)

      return None;
