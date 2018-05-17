from __future__ import print_function
import math
import numpy as np
import parameters as par
from ExcessZ import g
from Excesspl import Rpkpcfunc
from err_NT import errNT
from galpyMWBHRfo import MWBHRfo


def calhb(bdeg, sigb, ldeg, sigl, dkpc, sigd, Har):           
      b = bdeg*par.degtorad
      l = ldeg*par.degtorad
      zkpc = dkpc*math.sin(b)

      azbcnt = g(zkpc)*math.sin(b) #s^-1
      errnt = errNT(bdeg, sigb, dkpc, sigd) #s^-1
      ExcRforceBH = MWBHRfo(bdeg,ldeg,dkpc) #s^-1


      print ("Excess_parallel(galpy-Rforce,with BH), Excess_z_NT95 = ", ExcRforceBH,", ", azbcnt) 
 
      return None;
