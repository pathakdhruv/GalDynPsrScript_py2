from __future__ import print_function
import math
import numpy as np
import parameters as par
from Excesspl import Rpkpcfunc
from calA import cala, Expla, Exza, Errpla, Errza
from calB import calb, Explb, Exzb, Errplb, Errzb
from calC import calc, Explc, Exzc, Errplc, Errzc
from calD import cald, Expld, Exzd, Errpld, Errzd
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

from Shk import shk, Exshk, errShk
from err_Rp import errRp
from err_zkpc import errz
from pdotint import Pdotintcalerr, Pdotintcal

def allcal(bdeg, sigb, ldeg, sigl, dkpc, sigd, Har): 
      flag = 1
      inp = raw_input("Choose Your Option A/B/C/D/Ea/Eb/Fa/Fb/Ga/Gb/Ha/Hb/Ia/Ib/Ja/Jb/Ka/Kb/La/Lb (Check README for details): ")
      if inp == 'A' or inp == 'a' :
         cala(bdeg, sigb, ldeg, sigl, dkpc, sigd, Har)
         Ex_pl = Expla()
         Ex_z = Exza()
         if Har == 0:
           errpl = Errpla()
           errper = Errza()
         flag2 = 1
      elif inp == 'B' or inp == 'b' :
         calb(bdeg, sigb, ldeg, sigl, dkpc, sigd, Har)
         Ex_pl = Explb()
         Ex_z = Exzb()
         if Har == 0:
           errpl = Errplb()
           errper = Errzb()
         flag2 = 1
      elif inp == 'C' or inp == 'c' :
         calc(bdeg, sigb, ldeg, sigl, dkpc, sigd, Har)
         Ex_pl = Explc()
         Ex_z = Exzc()
         if Har == 0:
           errpl = Errplc()
           errper = Errzc()
         flag2 = 1
      elif inp == 'D' or inp == 'd' :
         cald(bdeg, sigb, ldeg, sigl, dkpc, sigd, Har)
         Ex_pl = Expld()
         Ex_z = Exzd()
         if Har == 0:
           errpl = Errpld()
           errper = Errzd()
         flag2 = 1
      elif inp == 'Ea' or inp == 'ea' :
         calea(bdeg, sigb, ldeg, sigl, dkpc, sigd, Har)
         Ex_pl = Explea()
         Ex_z = Exzea()
         flag2 = 0
      elif inp == 'Eb' or inp == 'eb' :
         caleb(bdeg, sigb, ldeg, sigl, dkpc, sigd, Har)
         Ex_pl = Expleb()
         Ex_z = Exzeb()      
         flag2 = 0   
      elif inp == 'Fa' or inp == 'fa' :
         calfa(bdeg, sigb, ldeg, sigl, dkpc, sigd, Har)
         Ex_pl = Explfa()
         Ex_z = Exzfa()
         flag2 = 0
      elif inp == 'Fb' or inp == 'fb' :
         calfb(bdeg, sigb, ldeg, sigl, dkpc, sigd, Har)
         Ex_pl = Explfb()
         Ex_z = Exzfb()
         flag2 = 0
      elif inp == 'Ga' or inp == 'ga' :
         calga(bdeg, sigb, ldeg, sigl, dkpc, sigd, Har)
         Ex_pl = Explga()
         Ex_z = Exzga()
         flag2 = 0
      elif inp == 'Gb' or inp == 'gb' :
         calgb(bdeg, sigb, ldeg, sigl, dkpc, sigd, Har)
         Ex_pl = Explgb()
         Ex_z = Exzgb()
         flag2 = 0
      elif inp == 'Ha' or inp == 'ha' :
         calha(bdeg, sigb, ldeg, sigl, dkpc, sigd, Har)
         Ex_pl = Explha()
         Ex_z = Exzha()
         flag2 = 0
      elif inp == 'Hb' or inp == 'hb' :
         calhb(bdeg, sigb, ldeg, sigl, dkpc, sigd, Har)
         Ex_pl = Explhb()
         Ex_z = Exzhb()
         flag2 = 0
      elif inp == 'Ia' or inp == 'ia' :
         calia(bdeg, sigb, ldeg, sigl, dkpc, sigd, Har)
         Ex_pl = Explia()
         Ex_z = Exzia()
         flag2 = 0
      elif inp == 'Ib' or inp == 'ib' :
         calib(bdeg, sigb, ldeg, sigl, dkpc, sigd, Har)
         Ex_pl = Explib()
         Ex_z = Exzib()
         flag2 = 0
      elif inp == 'Ja' or inp == 'ja' :
         calja(bdeg, sigb, ldeg, sigl, dkpc, sigd, Har)
         Ex_pl = Explja()
         Ex_z = Exzja()
         flag2 = 0
      elif inp == 'Jb' or inp == 'jb' :
         caljb(bdeg, sigb, ldeg, sigl, dkpc, sigd, Har)
         Ex_pl = Expljb()
         Ex_z = Exzjb()
         flag2 = 0
      elif inp == 'Ka' or inp == 'ka' :
         calka(bdeg, sigb, ldeg, sigl, dkpc, sigd, Har)
         Ex_pl = Explka()
         Ex_z = Exzka()
         flag2 = 0
      elif inp == 'Kb' or inp == 'kb' :
         calkb(bdeg, sigb, ldeg, sigl, dkpc, sigd, Har)
         Ex_pl = Explkb()
         Ex_z = Exzkb()
         flag2 = 0
      elif inp == 'La' or inp == 'la' :
         calla(bdeg, sigb, ldeg, sigl, dkpc, sigd, Har)
         Ex_pl = Explla()
         Ex_z = Exzla()
         flag2 = 0
      elif inp == 'Lb' or inp == 'lb' :
         callb(bdeg, sigb, ldeg, sigl, dkpc, sigd, Har)
         Ex_pl = Expllb()
         Ex_z = Exzlb()
         flag2 = 0
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
            errshk = errShk()
         elif inp2 == 'N' or inp2 == 'n' :
            print ("Ok")
            Ex_shk = 0.0
            errshk = 0.0
         else:
            print ("Invalid Input") 

         inp3 = raw_input("Do you want the intrinsic period derivative?(Y/N): ")
         if inp3 == "Y" or inp3 == "y" :
            if flag2 == 1 and Har == 0:        
               Pdotintcalerr(Ex_pl, Ex_z, Ex_shk, errpl, errper, errshk)
            else:
               Pdotintcal(Ex_pl, Ex_z, Ex_shk,flag2)

         elif inp3 == "N" or inp3 == "n" :
            print ("Ok") 
         else:
            print ("Invalid Input")    
      print ("\n Please round off the outputs appropriately \n")
      return None;
