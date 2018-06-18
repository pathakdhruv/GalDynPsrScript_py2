from __future__ import print_function
import math
import numpy as np
import parameters as par
from Excesspl import Rpkpcfunc
from calA import cala, Expla, Exza
from calB import calb, Explb, Exzb
from calC import calc, Explc, Exzc
from calD import cald, Expld, Exzd
from calEa import calea, Explea, Exzea
from calEb import caleb, Expleb, Exzeb
from calFa import calfa, Explfa, Exzfa
from calFb import calfb, Explfb, Exzfb
from calGa import calga, Explga, Exzga
from calGb import calgb, Explgb, Exzgb
from calHa import calha, Explha, Exzha
from calHb import calhb, Explhb, Exzhb
from calIa import calia, Explia, Exzia
from calIb import calib, Explib, Exzib
from calJa import calja, Explja, Exzja
from calJb import caljb, Expljb, Exzjb
from calKa import calka, Explka, Exzka
from calKb import calkb, Explkb, Exzkb
from calLa import calla, Explla, Exzla
from calLb import callb, Expllb, Exzlb

from Shk import shk, Exshk
from err_Rp import errRp
from err_zkpc import errz
from pdotint import Pdotintcal

def allcal(bdeg, sigb, ldeg, sigl, dkpc, sigd, Har): 
      flag = 1
      inp = raw_input("Choose Your Option A/B/C/D/Ea/Eb/Fa/Fb/Ga/Gb/Ha/Hb/Ia/Ib/Ja/Jb/Ka/Kb/La/Lb (Check README for details): ")
      if inp == 'A' or inp == 'a' :
         cala(bdeg, sigb, ldeg, sigl, dkpc, sigd, Har)
         Ex_pl = Expla()
         Ex_z = Exza()
      elif inp == 'B' or inp == 'b' :
         calb(bdeg, sigb, ldeg, sigl, dkpc, sigd, Har)
         Ex_pl = Explb()
         Ex_z = Exzb()
      elif inp == 'C' or inp == 'c' :
         calc(bdeg, sigb, ldeg, sigl, dkpc, sigd, Har)
         Ex_pl = Explc()
         Ex_z = Exzc()
      elif inp == 'D' or inp == 'd' :
         cald(bdeg, sigb, ldeg, sigl, dkpc, sigd, Har)
         Ex_pl = Expld()
         Ex_z = Exzd()
      elif inp == 'Ea' or inp == 'ea' :
         calea(bdeg, sigb, ldeg, sigl, dkpc, sigd, Har)
         Ex_pl = Explea()
         Ex_z = Exzea()
      elif inp == 'Eb' or inp == 'eb' :
         caleb(bdeg, sigb, ldeg, sigl, dkpc, sigd, Har)
         Ex_pl = Expleb()
         Ex_z = Exzeb()         
      elif inp == 'Fa' or inp == 'fa' :
         calfa(bdeg, sigb, ldeg, sigl, dkpc, sigd, Har)
         Ex_pl = Explfa()
         Ex_z = Exzfa()
      elif inp == 'Fb' or inp == 'fb' :
         calfb(bdeg, sigb, ldeg, sigl, dkpc, sigd, Har)
         Ex_pl = Explfb()
         Ex_z = Exzfb()
      elif inp == 'Ga' or inp == 'ga' :
         calga(bdeg, sigb, ldeg, sigl, dkpc, sigd, Har)
         Ex_pl = Explga()
         Ex_z = Exzga()
      elif inp == 'Gb' or inp == 'gb' :
         calgb(bdeg, sigb, ldeg, sigl, dkpc, sigd, Har)
         Ex_pl = Explgb()
         Ex_z = Exzgb()
      elif inp == 'Ha' or inp == 'ha' :
         calha(bdeg, sigb, ldeg, sigl, dkpc, sigd, Har)
         Ex_pl = Explha()
         Ex_z = Exzha()
      elif inp == 'Hb' or inp == 'hb' :
         calhb(bdeg, sigb, ldeg, sigl, dkpc, sigd, Har)
         Ex_pl = Explhb()
         Ex_z = Exzhb()
      elif inp == 'Ia' or inp == 'ia' :
         calia(bdeg, sigb, ldeg, sigl, dkpc, sigd, Har)
         Ex_pl = Explia()
         Ex_z = Exzia()
      elif inp == 'Ib' or inp == 'ib' :
         calib(bdeg, sigb, ldeg, sigl, dkpc, sigd, Har)
         Ex_pl = Explib()
         Ex_z = Exzib()
      elif inp == 'Ja' or inp == 'ja' :
         calja(bdeg, sigb, ldeg, sigl, dkpc, sigd, Har)
         Ex_pl = Explja()
         Ex_z = Exzja()
      elif inp == 'Jb' or inp == 'jb' :
         caljb(bdeg, sigb, ldeg, sigl, dkpc, sigd, Har)
         Ex_pl = Expljb()
         Ex_z = Exzjb()
      elif inp == 'Ka' or inp == 'ka' :
         calka(bdeg, sigb, ldeg, sigl, dkpc, sigd, Har)
         Ex_pl = Explka()
         Ex_z = Exzka()
      elif inp == 'Kb' or inp == 'kb' :
         calkb(bdeg, sigb, ldeg, sigl, dkpc, sigd, Har)
         Ex_pl = Explkb()
         Ex_z = Exzkb()
      elif inp == 'La' or inp == 'la' :
         calla(bdeg, sigb, ldeg, sigl, dkpc, sigd, Har)
         Ex_pl = Explla()
         Ex_z = Exzla()
      elif inp == 'Lb' or inp == 'lb' :
         callb(bdeg, sigb, ldeg, sigl, dkpc, sigd, Har)
         Ex_pl = Expllb()
         Ex_z = Exzlb()
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
            Ex_shk = Exshk()
         elif inp2 == 'N' or inp2 == 'n' :
            print ("Ok")
            Ex_shk = 0.0
         else:
            print ("Invalid Input") 

         inp3 = raw_input("Do you want the intrinsic period derivative?(Y/N): ")
         if inp3 == "Y" or inp3 == "y" :
            Pdotintcal(Ex_pl, Ex_z, Ex_shk)
         elif inp3 == "N" or inp3 == "n" :
            print ("Ok") 
         else:
            print ("Invalid Input")    
      
      return None;
