from __future__ import print_function
import math
import numpy as np
import parameters as par
from Excesspl import aplmod
from Excesspl import Rpkpcfunc
from Excesspl import Vprat
from err_excesspl_Reid import err_Reid14
from galpyMWZfo import MWZfo


def calfa(bdeg, sigb, ldeg, sigl, dkpc, sigd, Har): 
      global excpl,exz          
      b = bdeg*par.degtorad
      l = ldeg*par.degtorad
      zkpc = dkpc*math.sin(b)

      adrc = aplmod(dkpc,b,l)*math.cos(b) #s^-1
      errReid = err_Reid14(bdeg, sigb, ldeg, sigl, dkpc, sigd) #s^-1

      Excz = MWZfo(bdeg,ldeg,dkpc)#s^-1


      print ("Excess_parallel_Reid2014,  Excess_z_galpy(without BH) = ", adrc,", ", Excz)
      excpl = adrc
      exz = Excz
      return None;

def Explfa():
   return excpl;

def Exzfa():
   return exz;
