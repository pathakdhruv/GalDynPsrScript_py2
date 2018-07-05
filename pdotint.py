from __future__ import print_function
import math


def Pdotintcalerr(Ex_pl, Ex_z, Ex_shk, errpl, errz, errshk):
   a = Ex_pl
   b = Ex_z
   c = Ex_shk
   pdotbypdyn = a+b+c
   dtos = 24.0*3600.0
   inp = raw_input("Do you want (1)- Only intrinsic spin period derivative, (2)- Only intrinsic orbital period decay, or, (3)- Both? Choose 1, 2, or 3: ")

   if inp == "1":
       Psraw,sigPsraw = raw_input("\nEnter spin period- Ps (s), error in spin period [separated by a comma] ").split((','))
       Psdot_obsraw,sigPsdot_obsraw  = raw_input("Enter observed spin period derivative- Psdot_obs, error in observed spin period derivative [separated by a comma] ").split((','))
       Ps = float(Psraw)
       sigPs = float(sigPsraw)
       Psdot_obs = float(Psdot_obsraw)
       sigPsdot_obs = float(sigPsdot_obsraw)
       Psdotint = Psdot_obs-(pdotbypdyn*Ps)

       Err_Psdot_Expl = ((Ps*errpl)**2. + (a*sigPs)**2.)**0.5
       Err_Psdot_Exz =  ((Ps*errz)**2. + (b*sigPs)**2.)**0.5
       Err_Psdot_Shk = ((Ps*errshk)**2. + (c*sigPs)**2.)**0.5
       err_ab = ((errpl)**2.+(errz)**2.)**0.5
       Err_Psdot_Gal = ((Ps*err_ab)**2.+((a+b)*sigPs)**2.)**0.5
       err_pdotbypdyn = ((errpl)**2.+(errz)**2.+(errshk)**2.)**0.5
       err_pdotbypdynPs = ((Ps*err_pdotbypdyn)**2.+(pdotbypdyn*sigPs)**2.)**0.5
       Err_Psdot_int = ((err_pdotbypdynPs)**2.+(sigPsdot_obs )**2.)**0.5


       
       if Err_Psdot_Expl<0.0:
          print ("\nPsdot_Expl = -(", -a*Ps, "+/-", abs(Err_Psdot_Expl),")")         
       else: 
          print ("\nPsdot_Expl = ", a*Ps, "+/-", Err_Psdot_Expl)

       print ("Psdot_Exz = -(", abs(b*Ps), "+/-", abs(Err_Psdot_Exz),")")

       if Err_Psdot_Gal<0.0:
          print ("Psdot_Gal (Psdot_Expl + Psdot_Exz) = -(", -(a+b)*Ps, "+/-", abs(Err_Psdot_Gal),")")        
       else:
          print ("Psdot_Gal (Psdot_Expl + Psdot_Exz) = ", (a+b)*Ps, "+/-", Err_Psdot_Gal)

       print ("Psdot_Shk = ", c*Ps, "+/-", Err_Psdot_Shk)

       if Err_Psdot_int<0.0:
          print ("Psdot_int = -(", -Psdotint, "+/-", abs(Err_Psdot_int),")")
       else:
          print ("Psdot_int = ", Psdotint, "+/-", Err_Psdot_int)

   elif inp == "2":
       Pbdraw,sigPbdraw = raw_input("\nEnter orbital period- Pb (days), error in orbital period [separated by a comma] ").split((','))
       Pbdot_obsraw,sigPbdot_obsraw  = raw_input("Enter observed orbital period derivative- Pbdot_obs, error in observed orbital period derivative [separated by a comma] ").split((','))
       Pbd = float(Pbdraw)
       sigPbd = float(sigPbdraw)
       Pbdot_obs = float(Pbdot_obsraw)
       sigPbdot_obs = float(sigPbdot_obsraw)
       Pbs = Pbd*dtos
       Pbdotint = Pbdot_obs-(pdotbypdyn*Pbs)

       Err_Pbdot_Expl = ((Pbs*errpl)**2. + (a*sigPbd*dtos)**2.)**0.5
       Err_Pbdot_Exz =  ((Pbs*errz)**2. + (b*sigPbd*dtos)**2.)**0.5
       Err_Pbdot_Shk = ((Pbs*errshk)**2. + (c*sigPbd*dtos)**2.)**0.5
       err_ab = ((errpl)**2.+(errz)**2.)**0.5
       Err_Pbdot_Gal = ((Pbs*err_ab)**2.+((a+b)*sigPbd*dtos)**2.)**0.5
       err_pdotbypdyn = ((errpl)**2.+(errz)**2.+(errshk)**2.)**0.5
       err_pdotbypdynPbs = ((Pbs*err_pdotbypdyn)**2.+(pdotbypdyn*sigPbd*dtos)**2.)**0.5
       Err_Pbdot_int = ((err_pdotbypdynPbs)**2.+(sigPbdot_obs)**2.)**0.5


       if Err_Pbdot_Expl<0.0:
          print ("\nPbdot_Expl = -(", -a*Pbs, "+/-", abs(Err_Pbdot_Expl),")")         
       else: 
          print ("\nPbdot_Expl = ", a*Pbs, "+/-", Err_Pbdot_Expl)

       print ("Pbdot_Exz = -(", abs(b*Pbs), "+/-", abs(Err_Pbdot_Exz),")")

       if Err_Pbdot_Gal<0.0:
          print ("Pbdot_Gal (Pbdot_Expl + Pbdot_Exz) = -(", -(a+b)*Pbs, "+/-", abs(Err_Pbdot_Gal),")")        
       else:
          print ("Pbdot_Gal (Pbdot_Expl + Pbdot_Exz) = ", (a+b)*Pbs, "+/-", Err_Pbdot_Gal)

       print ("Pbdot_Shk = ", c*Pbs, "+/-", Err_Pbdot_Shk)

       if Err_Pbdot_int<0.0:
          print ("Pbdot_int = -(", -Pbdotint, "+/-", abs(Err_Pbdot_int),")")
       else:
          print ("Pbdot_int = ", Pbdotint, "+/-", Err_Pbdot_int)

   elif inp == "3":
       Psraw,sigPsraw = raw_input("\nEnter spin period- Ps (s), error in spin period [separated by a comma] ").split((','))
       Pbdraw,sigPbdraw = raw_input("Enter orbital period- Pb (days), error in orbital period [separated by a comma] ").split((','))
       Psdot_obsraw,sigPsdot_obsraw  = raw_input("Enter observed spin period derivative- Psdot_obs, error in observed spin period derivative [separated by a comma] ").split((','))
       Pbdot_obsraw,sigPbdot_obsraw  = raw_input("Enter observed orbital period derivative- Pbdot_obs, error in observed orbital period derivative [separated by a comma] ").split((','))




       Ps = float(Psraw)
       sigPs = float(sigPsraw)
       Psdot_obs = float(Psdot_obsraw)
       sigPsdot_obs = float(sigPsdot_obsraw)
       Psdotint = Psdot_obs-(pdotbypdyn*Ps)
       Err_Psdot_Expl = ((Ps*errpl)**2. + (a*sigPs)**2.)**0.5
       Err_Psdot_Exz =  ((Ps*errz)**2. + (b*sigPs)**2.)**0.5
       Err_Psdot_Shk = ((Ps*errshk)**2. + (c*sigPs)**2.)**0.5
       err_ab = ((errpl)**2.+(errz)**2.)**0.5
       Err_Psdot_Gal = ((Ps*err_ab)**2.+((a+b)*sigPs)**2.)**0.5
       err_pdotbypdyn = ((errpl)**2.+(errz)**2.+(errshk)**2.)**0.5
       err_pdotbypdynPs = ((Ps*err_pdotbypdyn)**2.+(pdotbypdyn*sigPs)**2.)**0.5
       Err_Psdot_int = ((err_pdotbypdynPs)**2.+(sigPsdot_obs )**2.)**0.5



       Pbd = float(Pbdraw)
       sigPbd = float(sigPbdraw)
       Pbdot_obs = float(Pbdot_obsraw)
       sigPbdot_obs = float(sigPbdot_obsraw)
       Pbs = Pbd*dtos
       Pbdotint = Pbdot_obs-(pdotbypdyn*Pbs)
       Err_Pbdot_Expl = ((Pbs*errpl)**2. + (a*sigPbd*dtos)**2.)**0.5
       Err_Pbdot_Exz =  ((Pbs*errz)**2. + (b*sigPbd*dtos)**2.)**0.5
       Err_Pbdot_Shk = ((Pbs*errshk)**2. + (c*sigPbd*dtos)**2.)**0.5
       err_ab = ((errpl)**2.+(errz)**2.)**0.5
       Err_Pbdot_Gal = ((Pbs*err_ab)**2.+((a+b)*sigPbd*dtos)**2.)**0.5
       err_pdotbypdyn = ((errpl)**2.+(errz)**2.+(errshk)**2.)**0.5
       err_pdotbypdynPbs = ((Pbs*err_pdotbypdyn)**2.+(pdotbypdyn*sigPbd*dtos)**2.)**0.5
       Err_Pbdot_int = ((err_pdotbypdynPbs)**2.+(sigPbdot_obs)**2.)**0.5


   

       if Err_Psdot_Expl<0.0:
          print ("\nPsdot_Expl = -(", -a*Ps, "+/-", abs(Err_Psdot_Expl),")")         
       else: 
          print ("\nPsdot_Expl = ", a*Ps, "+/-", Err_Psdot_Expl)

       print ("Psdot_Exz = -(", abs(b*Ps), "+/-", abs(Err_Psdot_Exz),")")

       if Err_Psdot_Gal<0.0:
          print ("Psdot_Gal (Psdot_Expl + Psdot_Exz) = -(", -(a+b)*Ps, "+/-", abs(Err_Psdot_Gal),")")        
       else:
          print ("Psdot_Gal (Psdot_Expl + Psdot_Exz) = ", (a+b)*Ps, "+/-", Err_Psdot_Gal)

       print ("Psdot_Shk = ", c*Ps, "+/-", Err_Psdot_Shk)

       if Err_Psdot_int<0.0:
          print ("Psdot_int = -(", -Psdotint, "+/-", abs(Err_Psdot_int),")")
       else:
          print ("Psdot_int = ", Psdotint, "+/-", Err_Psdot_int)



       if Err_Pbdot_Expl<0.0:
          print ("Pbdot_Expl = -(", -a*Pbs, "+/-", abs(Err_Pbdot_Expl),")")         
       else: 
          print ("Pbdot_Expl = ", a*Pbs, "+/-", Err_Pbdot_Expl)

       print ("Pbdot_Exz = -(", abs(b*Pbs), "+/-", abs(Err_Pbdot_Exz),")")

       if Err_Pbdot_Gal<0.0:
          print ("Pbdot_Gal (Pbdot_Expl + Pbdot_Exz) = -(", -(a+b)*Pbs, "+/-", abs(Err_Pbdot_Gal),")")        
       else:
          print ("Pbdot_Gal (Pbdot_Expl + Pbdot_Exz) = ", (a+b)*Pbs, "+/-", Err_Pbdot_Gal)

       print ("Pbdot_Shk = ", c*Pbs, "+/-", Err_Pbdot_Shk)

       if Err_Pbdot_int<0.0:
          print ("Pbdot_int = -(", -Pbdotint, "+/-", abs(Err_Pbdot_int),")")
       else:
          print ("Pbdot_int = ", Pbdotint, "+/-", Err_Pbdot_int)


   else:
       print ("Invalid Input") 


   return None;



def Pdotintcal(Ex_pl, Ex_z, Ex_shk,flag2):
   a = Ex_pl
   b = Ex_z
   c = Ex_shk
   pdotbypdyn = a+b+c
   inp = raw_input("Do you want (1)- Only intrinsic spin period derivative, (2)- Only intrinsic orbital period decay, or, (3)- Both? Choose 1, 2, or 3: ")
   if flag2 == 0:
      print ("\nNo need to input errors as we are using galpy\n")
   if inp == "1":
       Psraw = raw_input("\nEnter Ps (s) = ")
       Psdot_obsraw = raw_input("Enter Psdot_obs = ")

       if "," in Psraw:
          a1 = Psraw.split(',')[0]
          Ps = float(a1)
       else:
          Ps = float(Psraw)

       if "," in Psdot_obsraw:
          a2 = Psdot_obsraw.split(',')[0]
          Psdot_obs = float(a2)
       else:
          Psdot_obs = float(Psdot_obsraw)

       Psdotint = Psdot_obs-(pdotbypdyn*Ps)

       print ("\nPsdot_Expl = ", a*Ps)
       print ("Psdot_Exz = ", b*Ps)
       print ("Psdot_Gal (Psdot_Expl + Psdot_Exz) = ", (a+b)*Ps)
       print ("Psdot_Shk = ", c*Ps)
       print ("Psdot_int = ", Psdotint)
      
   elif inp == "2":

       Pbdraw = raw_input("\nEnter Pb (days) = ")
       Pbdot_obsraw = raw_input("Enter Pbdot_obs = ")

       if "," in Pbdraw:
          a1 = Pbdraw.split(',')[0]
          Pbd = float(a1)
       else:
          Pbd = float(Pbdraw)

       if "," in Pbdot_obsraw:
          a2 = Pbdot_obsraw.split(',')[0]
          Pbdot_obs = float(a2)
       else:
          Pbdot_obs = float(Pbdot_obsraw)


       Pbs = Pbd*24.0*3600.0
       Pbdotint = Pbdot_obs-(pdotbypdyn*Pbs)

       print ("\nPbdot_Expl = ", a*Pbs)
       print ("Pbdot_Exz = ", b*Pbs) 
       print ("Pbdot_Gal (Pbdot_Expl + Pbdot_Exz) = ", (a+b)*Pbs)
       print ("Pbdot_Shk = ", c*Pbs)
       print ("Pbdot_int = ", Pbdotint)

   elif inp == "3":



       Psraw = raw_input("\nEnter Ps (s) = ")
       if "," in Psraw:
          a1 = Psraw.split(',')[0]
          Ps = float(a1)
       else:
          Ps = float(Psraw)

       Pbdraw = raw_input("Enter Pb (days) = ")
       if "," in Pbdraw:
          b1 = Pbdraw.split(',')[0]
          Pbd = float(b1)
       else:
          Pbd = float(Pbdraw)

       Psdot_obsraw = raw_input("Enter Psdot_obs = ")
       if "," in Psdot_obsraw:
          a2 = Psdot_obsraw.split(',')[0]
          Psdot_obs = float(a2)
       else:
          Psdot_obs = float(Psdot_obsraw)

       Pbdot_obsraw = raw_input("Enter Pbdot_obs = ")
       if "," in Pbdot_obsraw:
          b2 = Pbdot_obsraw.split(',')[0]
          Pbdot_obs = float(b2)
       else:
          Pbdot_obs = float(Pbdot_obsraw)


       Psdotint = Psdot_obs-(pdotbypdyn*Ps)
       Pbs = Pbd*24.0*3600.0
       Pbdotint = Pbdot_obs-(pdotbypdyn*Pbs)


       print ("\nPsdot_Expl = ", a*Ps)
       print ("Psdot_Exz = ", b*Ps)
       print ("Psdot_Gal (Psdot_Expl + Psdot_Exz) = ", (a+b)*Ps)
       print ("Psdot_Shk = ", c*Ps)
       print ("Psdot_int = ", Psdotint)

   
       print ("Pbdot_Expl = ", a*Pbs)
       print ("Pbdot_Exz = ", b*Pbs)
       print ("Pbdot_Gal (Pbdot_Expl + Pbdot_Exz) = ", (a+b)*Pbs)
       print ("Pbdot_Shk = ", c*Pbs)
       print ("Pbdot_int = ", Pbdotint)


   else:
       print ("Invalid Input") 


   return None;


