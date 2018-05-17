from __future__ import print_function
import math
import parameters as par
from AllCal import allcal

def ExcessGalfunc():
    global Har
    Har = 0

    ldegr, siglr = raw_input("Enter (Galactic longitude) l in degrees (0 to 360), error in l(sigl) [separated by comma]:  ").split((','))
    
    bdegr, sigbr = raw_input("Enter (Galactic latitude) b in degrees (-90 to 90), error in b(sigb) [separated by comma]:  ").split((','))

    dkpcr, sigdr = raw_input("Enter distance of the pulsar (from the sun) in kpc, error in d(sigd) [separated by comma]:  ").split((','))
   
    bdeg = float(bdegr)
    sigb = float(sigbr)
    ldeg = float(ldegr)
    sigl = float(siglr)
    dkpc = float(dkpcr)
    sigd = float(sigdr)

    
    if bdeg==0.0 and ldeg == 0.0 and dkpc == par.Rskpc:
       print ("This is the Galactic Centre. Here apl term has a division by zero!")

    elif bdeg<=90.0 and bdeg >=-90.0 and ldeg <=360.0 and ldeg >=0.0 :
       allcal(bdeg, sigb, ldeg, sigl, dkpc, sigd,Har)

    else:
       print ("Invalid input. Check b and l values again.")
    return None;


