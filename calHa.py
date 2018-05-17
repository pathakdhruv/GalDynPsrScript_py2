from __future__ import print_function
import math
import numpy as np
import parameters as par
from ExcessZ import g
from Excesspl import Rpkpcfunc
from err_NT import errNT
from galpyMWRfo import MWRfo


def calha(bdeg, sigb, ldeg, sigl, dkpc, sigd, Har):           
      b = bdeg*par.degtorad
      l = ldeg*par.degtorad
      zkpc = dkpc*math.sin(b)

      azbcnt = g(zkpc)*math.sin(b) #s^-1
      errnt = errNT(bdeg, sigb, dkpc, sigd) #s^-1
      
      ExcRforce = MWRfo(bdeg,ldeg,dkpc)


      print ("Excess_parallel(galpy-Rforce,without BH), Excess_z_NT95 = ", ExcRforce,", ", azbcnt)

      return None;
