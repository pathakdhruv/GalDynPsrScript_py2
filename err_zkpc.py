import math
import numpy as np
import parameters as par
global bdeg, sigb, dkpc, sigd, b

def errz(bdeg, sigb, dkpc, sigd):
    b = bdeg*par.degtorad
    
    err_zkpcsq = pow(dkpc*math.cos(b),2.0)*pow(sigb,2.0) + pow(math.sin(b),2.0)*pow(sigd,2.0)
    err_zkpc = pow(err_zkpcsq,0.5) 
    return err_zkpc;    
