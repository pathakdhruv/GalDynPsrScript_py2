from __future__ import print_function
import math
import numpy as np
import parameters as par
from Excesspl import Rpkpcfunc
from galpyMWZfo import MWZfo
from galpyMWpl import MWpl

def calka(bdeg, sigb, ldeg, sigl, dkpc, sigd, Har):           
      b = bdeg*par.degtorad
      l = ldeg*par.degtorad
      zkpc = dkpc*math.sin(b)

      Excpl = MWpl(bdeg,ldeg,dkpc) #s^-1
      Excz = MWZfo(bdeg,ldeg,dkpc)#s^-1


      print ("Excess_parallel_galpy(from Vp/Vs, without BH),   Excess_z_galpy(without BH) = ", Excpl,", ", Excz)


      return None;
