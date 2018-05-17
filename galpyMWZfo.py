import math
from galpy.potential import MWPotential2014
from galpy.util import bovy_conversion
from astropy import units
from galpy.potential import evaluatezforces
import parameters as par
from Excesspl import Rpkpcfunc


def MWZfo(bdeg,ldeg,dkpc):

    b = bdeg*par.degtorad
    l = ldeg*par.degtorad
    Rskpc = par.Rskpc
    Vs = par.Vs
    conversion = par.conversion
    Rpkpc = Rpkpcfunc(dkpc,b,l,Rskpc)
    zkpc = dkpc*math.sin(b)

    zf1 = evaluatezforces(MWPotential2014, Rpkpc/Rskpc,zkpc/Rskpc)*bovy_conversion.force_in_kmsMyr(Vs,Rskpc)
    Excz = zf1*conversion*math.sin(b)#s-1
    return Excz;


