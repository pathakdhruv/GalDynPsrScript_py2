from __future__ import print_function
import math
import numpy as np
import parameters as par
from Excesspl import Rpkpcfunc
from calA import cala
from calB import calb
from calC import calc
from calD import cald
from calEa import calea
from calEb import caleb
from calFa import calfa
from calFb import calfb
from calGa import calga
from calGb import calgb
from calHa import calha
from calHb import calhb
from calIa import calia
from calIb import calib
from calJa import calja
from calJb import caljb
from calKa import calka
from calKb import calkb
from calLa import calla
from calLb import callb

from Shk import shk
from err_Rp import errRp
from err_zkpc import errz


def allcal(bdeg, sigb, ldeg, sigl, dkpc, sigd, Har): 
      flag = 1
      inp = raw_input("Choose Your Option A/B/C/D/Ea/Eb/Fa/Fb/Ga/Gb/Ha/Hb/Ia/Ib/Ja/Jb/Ka/Kb/La/Lb (Check README for details): ")
      if inp == 'A' or inp == 'a' :
         cala(bdeg, sigb, ldeg, sigl, dkpc, sigd, Har)
      elif inp == 'B' or inp == 'b' :
         calb(bdeg, sigb, ldeg, sigl, dkpc, sigd, Har)
      elif inp == 'C' or inp == 'c' :
         calc(bdeg, sigb, ldeg, sigl, dkpc, sigd, Har)
      elif inp == 'D' or inp == 'd' :
         cald(bdeg, sigb, ldeg, sigl, dkpc, sigd, Har)
      elif inp == 'Ea' or inp == 'ea' :
         calea(bdeg, sigb, ldeg, sigl, dkpc, sigd, Har)
      elif inp == 'Eb' or inp == 'eb' :
         caleb(bdeg, sigb, ldeg, sigl, dkpc, sigd, Har)         
      elif inp == 'Fa' or inp == 'fa' :
         calfa(bdeg, sigb, ldeg, sigl, dkpc, sigd, Har)
      elif inp == 'Fb' or inp == 'fb' :
         calfb(bdeg, sigb, ldeg, sigl, dkpc, sigd, Har)
      elif inp == 'Ga' or inp == 'ga' :
         calga(bdeg, sigb, ldeg, sigl, dkpc, sigd, Har)
      elif inp == 'Gb' or inp == 'gb' :
         calgb(bdeg, sigb, ldeg, sigl, dkpc, sigd, Har)
      elif inp == 'Ha' or inp == 'ha' :
         calha(bdeg, sigb, ldeg, sigl, dkpc, sigd, Har)
      elif inp == 'Hb' or inp == 'hb' :
         calhb(bdeg, sigb, ldeg, sigl, dkpc, sigd, Har)
      elif inp == 'Ia' or inp == 'ia' :
         calia(bdeg, sigb, ldeg, sigl, dkpc, sigd, Har)
      elif inp == 'Ib' or inp == 'ib' :
         calib(bdeg, sigb, ldeg, sigl, dkpc, sigd, Har)
      elif inp == 'Ja' or inp == 'ja' :
         calja(bdeg, sigb, ldeg, sigl, dkpc, sigd, Har)
      elif inp == 'Jb' or inp == 'jb' :
         caljb(bdeg, sigb, ldeg, sigl, dkpc, sigd, Har)
      elif inp == 'Ka' or inp == 'ka' :
         calka(bdeg, sigb, ldeg, sigl, dkpc, sigd, Har)
      elif inp == 'Kb' or inp == 'kb' :
         calkb(bdeg, sigb, ldeg, sigl, dkpc, sigd, Har)
      elif inp == 'La' or inp == 'la' :
         calla(bdeg, sigb, ldeg, sigl, dkpc, sigd, Har)
      elif inp == 'Lb' or inp == 'lb' :
         callb(bdeg, sigb, ldeg, sigl, dkpc, sigd, Har)
      else:
         flag = 0
         print ("Invalid Input")
      if flag == 1:
          
         b = bdeg*par.degtorad
         l = ldeg*par.degtorad
         zkpc = dkpc*math.sin(b)
         errzkpc = errz(bdeg, sigb, dkpc, sigd)

         Rskpc = par.Rskpc    
         Rpkpc = Rpkpcfunc(dkpc,b,l,Rskpc)
         errRpkpc = errRp(bdeg, sigb, ldeg, sigl, dkpc, sigd)

         if Har==1:
            print ("Z value in kpc = ", zkpc)
            print ("Rp in kpc = ", Rpkpc)
            print ("We are not reporting errors as Harris catalogue does not contain any error. If you want error, enter inputs (l, b, d) with errors after choosing 'n' in the first step.")
         else:          
            print ("Z value in kpc = ", zkpc,"+/-",errzkpc)
            print ("Rp in kpc = ", Rpkpc,"+/-",errRpkpc)



      
         inp2 = raw_input("Do you want the Shklovskii term too?(Y/N): ")
         if inp2 == 'Y' or inp2 == 'y' :
            shk(dkpc, sigd)
         elif inp2 == 'N' or inp2 == 'n' :
            print ("Ok")
         else:
            print ("Invalid Input")     
      
      return None;
