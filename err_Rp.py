import math
import numpy as np
import parameters as par
from Excesspl import Rpkpcfunc


global c,Rskpc,Rpkpc,beta,t0,t1,dkpc,b,l,sigRs

def errRp(bdeg, sigb, ldeg, sigl, dkpc, sigd):
    sigRs = par.sigRs 
    c=par.c
    Rskpc=par.Rskpc
    Rs = Rskpc*par.kpctom
    b = bdeg*par.degtorad
    l = ldeg*par.degtorad   
    Rpkpc = Rpkpcfunc(dkpc,b,l,Rskpc)

    beta  = (dkpc*math.cos(b)/Rskpc) - math.cos(l)
    t0 = math.sin(l)*math.sin(l) + beta*beta
    t1 = pow(t0,0.5)


    def betabyd():
        a = math.cos(b)/Rskpc
        return a;

    def betabyb():
        a = -dkpc*math.sin(b)/Rskpc
        return a;

    def betabyl():
        a = math.sin(l)
        return a;

    def betabyRs():
        a = -dkpc*math.cos(b)/(Rskpc*Rskpc)
        return a;

    def Rpbyd():
        a = (Rskpc*beta*betabyd())/pow(t0,0.5)
        return a;

    def Rpbyb():
        a = (Rskpc*beta*betabyb())/pow(t0,0.5)
        return a;

    def Rpbyl():
        a = (Rskpc*(math.sin(l)*math.cos(l) + beta*betabyl()))/pow(t0,0.5)
        return a;

    def RpbyRs():
        a = pow(t0,0.5) + (Rskpc*beta*betabyRs())/pow(t0,0.5)
        return a;

    err_Rpsq = pow(Rpbyb(),2.0)*pow(sigb,2.0) + pow(Rpbyl(),2.0)*pow(sigl,2.0) + pow(Rpbyd(),2.0)*pow(sigd,2.0) + pow(RpbyRs(),2.0)*pow(sigRs,2.0)

    err_Rp = pow(err_Rpsq,0.5)
    return err_Rp;
    
