import math

global pi,degtorad,dtoyr,c,kpctom,yrts,Vs,Rskpc,conversion
pi = math.pi
degtorad= pi/180.0
dtoyr = 1.0/365.25
c = 299792458.0 #m/s
kpctom = 3.0856775814913675e+19
yrts = 365.25*24.0*3600.0
conversion = 1000.0/(c*yrts*pow(10.0,6.0))

# --- parameters and errors in those ----

Vs = 240.0 #km/s
sigVs = 8.0

Rskpc = 8.34 #kpc
sigRs = 0.16 


b0reid14 = -0.2 # km s^-1 kpc^-1, (dV/dR)
sigb0r = 0.4

b0dt91 = 0.00 # [-(Rs/V)*(dV/dR)]at R = Rs
sigb0dt = 0.03

