from __future__ import print_function
import math
import numpy as np
import parameters as par
from Excesspl import Rpkpcfunc
from galpyMWZfo import MWZfo
from galpyMWRfo import MWRfo

def calla(bdeg, sigb, ldeg, sigl, dkpc, sigd, Har):           
      b = bdeg*par.degtorad
      l = ldeg*par.degtorad
      zkpc = dkpc*math.sin(b)

      ExcRforce = MWRfo(bdeg,ldeg,dkpc) #s^-1
      Excz = MWZfo(bdeg,ldeg,dkpc)#s^-1

      print ("Excess_parallel(galpy-Rforce,without BH),   Excess_z_galpy(without BH) = ", ExcRforce,", ", Excz)

      return None;
