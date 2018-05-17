from __future__ import print_function
import math
import numpy as np
import parameters as par
from Excesspl import Rpkpcfunc
from galpyMWBHZfo import MWBHZfo
from galpyMWBHRfo import MWBHRfo

def callb(bdeg, sigb, ldeg, sigl, dkpc, sigd, Har):           
      b = bdeg*par.degtorad
      l = ldeg*par.degtorad
      zkpc = dkpc*math.sin(b)

      ExcRforceBH = MWBHRfo(bdeg,ldeg,dkpc) #s^-1
      Exczbh = MWBHZfo(bdeg,ldeg,dkpc) #s^-1


      print ("Excess_parallel(galpy-Rforce,with BH),   Excess_z_galpy(with BH) = ", ExcRforceBH,", ", Exczbh)


      return None;
